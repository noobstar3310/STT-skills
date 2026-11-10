#!/usr/bin/env python3
"""GitHub depth scan for STT candidate checks.

Usage:
  python3 github_scan.py <handle> [--lang Go] [--org anza-xyz --org solana-foundation] [--max-repos 15]

Needs the `gh` CLI, logged in (`gh auth login`). Read-only: only GET requests.
Prints a plain-text report with flags. See ../SKILL.md for how to read it.
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone


def gh(path, paginate=False):
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github+json", path]
    if paginate:
        cmd.insert(2, "--paginate")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        return None
    out = r.stdout.strip()
    if paginate and out.startswith("[") and "][" in out:
        out = out.replace("][", ",")
    try:
        return json.loads(out) if out else None
    except json.JSONDecodeError:
        return None


def days(iso):
    return datetime.fromisoformat(iso.replace("Z", "+00:00"))


def commit_spread(owner, repo, author):
    commits = gh(f"repos/{owner}/{repo}/commits?per_page=100&author={author}") or []
    if not isinstance(commits, list):
        return 0, 0, None, None
    dates = sorted({c["commit"]["author"]["date"][:10] for c in commits if c.get("commit")})
    first = dates[0] if dates else None
    last = dates[-1] if dates else None
    return len(commits), len(dates), first, last


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("handle")
    ap.add_argument("--lang", help="language to focus on, e.g. Go, Rust, TypeScript")
    ap.add_argument("--org", action="append", default=[], help="org to count merged PRs in (repeatable)")
    ap.add_argument("--max-repos", type=int, default=15)
    a = ap.parse_args()

    u = gh(f"users/{a.handle}")
    if not u:
        print(f"Could not read user {a.handle} (typo, deleted, or gh not logged in).")
        sys.exit(1)
    created = days(u["created_at"])
    age_years = (datetime.now(timezone.utc) - created).days / 365.25
    flags = []
    print(f"== {a.handle} ({u.get('name') or 'no name'})")
    print(f"Account created {u['created_at'][:10]} ({age_years:.1f} yrs) · public repos {u['public_repos']} · followers {u['followers']}")
    if age_years < 1:
        flags.append("NEW ACCOUNT (<1 yr)")

    repos = gh(f"users/{a.handle}/repos?per_page=100&sort=pushed") or []
    own = [r for r in repos if not r.get("fork")]
    forks = [r for r in repos if r.get("fork")]
    print(f"Own repos {len(own)} · forks {len(forks)}")
    if repos and not own:
        flags.append("FORKS ONLY")

    print("\nOwn repos (most recently pushed first):")
    print("name | language | created | pushed | stars | commits by user | distinct commit days | first..last | lang bytes")
    for r in own[: a.max_repos]:
        langs = gh(f"repos/{a.handle}/{r['name']}/languages") or {}
        lb = ", ".join(f"{k} {v//1024}KB" for k, v in sorted(langs.items(), key=lambda x: -x[1])[:3])
        n, d, first, last = commit_spread(a.handle, r["name"], a.handle)
        mark = ""
        if n >= 20 and d <= 2:
            mark = "  <- ONE-DAY REPO"
            flags.append(f"ONE-DAY REPO: {r['name']} ({n} commits over {d} day(s))")
        print(f"{r['name']} | {r.get('language')} | {r['created_at'][:10]} | {r['pushed_at'][:10]} | {r['stargazers_count']} | {n} | {d} | {first}..{last} | {lb}{mark}")

    # Merged PRs outside own account
    q = f"author:{a.handle}+type:pr+is:merged+-user:{a.handle}"
    res = gh(f"search/issues?q={q}&per_page=100") or {}
    items = res.get("items", [])
    print(f"\nMerged PRs in other people's repos: {res.get('total_count', 0)} (first 100 listed by repo)")
    by_repo = {}
    for it in items:
        repo = "/".join(it["repository_url"].split("/")[-2:])
        by_repo.setdefault(repo, []).append(it)
    small = 0
    sized = 0
    for repo, prs in sorted(by_repo.items(), key=lambda x: -len(x[1])):
        print(f"  {repo}: {len(prs)}")
    # size check on up to 10 PRs
    for it in items[:10]:
        repo = "/".join(it["repository_url"].split("/")[-2:])
        pr = gh(f"repos/{repo}/pulls/{it['number']}")
        if pr:
            sized += 1
            lines = pr.get("additions", 0) + pr.get("deletions", 0)
            if lines < 20:
                small += 1
            print(f"    sample: {repo}#{it['number']} '{it['title'][:60]}' +{pr.get('additions')} -{pr.get('deletions')} {it['html_url']}")
    if sized and small / sized > 0.6:
        flags.append(f"TINY PRS ({small}/{sized} sampled merged PRs < 20 lines)")

    for org in a.org:
        r = gh(f"search/issues?q=author:{a.handle}+type:pr+is:merged+org:{org}&per_page=1") or {}
        print(f"Merged PRs in org {org}: {r.get('total_count', 0)}")

    if a.lang:
        lang_own = [r for r in own if (r.get("language") or "").lower() == a.lang.lower()]
        print(f"\nOwn repos with main language {a.lang}: {len(lang_own)}")

    # Handle vs real name is judged by a human (handles are often nicknames).
    print("\nFLAGS: " + ("; ".join(flags) if flags else "none"))
    print("Next: open the biggest relevant PR / main repo and say what it actually is.")


if __name__ == "__main__":
    main()
