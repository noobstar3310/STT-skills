# STT Skills — candidate matchmaking for Claude Code

A pack of [Claude Code skills](https://docs.claude.com/en/docs/claude-code/skills) for **recruiting matchmaking**: take one job, screen candidates through four checks, and hand back ranked picks with the evidence on the page.

Built for technical recruiting in the Solana / crypto ecosystem at Superteam Talent, from real matchmaking runs. Works with any ATS that Claude can read (built against Airtable via MCP).

## The skills

| Skill | What it does |
| --- | --- |
| [`stt-match-job`](skills/stt-match-job/SKILL.md) | **Orchestrator.** Reads the JD + hiring notes, pulls the pipeline (every stage and inflow field), searches inflow and the talent pool, runs the 4 checks, ranks by core skill, and writes JD-fit tables, a side-by-side table, a reject list and a ready-to-paste team message |
| [`stt-check-location`](skills/stt-check-location/SKILL.md) | Separates hard rules (legal / nationality / timezone) from preferences, and widens the region in rings when the preferred one is empty |
| [`stt-check-seniority`](skills/stt-check-seniority/SKILL.md) | Real years from CV dates, level (IC / lead / head), and the **core-skill test** (production vs corporate work, main vs side language) |
| [`stt-check-github`](skills/stt-check-github/SKILL.md) | Public-code proof: account age, own vs forked repos, commit-day spread, merged PRs in real orgs. Flags one-day repos, forks-only and tiny PRs. Script: [`github_scan.py`](skills/stt-check-github/scripts/github_scan.py) |
| [`stt-check-identity`](skills/stt-check-identity/SKILL.md) | Fraud tells, do-not-pick and no-poach checks, plus a LinkedIn / X checklist for a human to verify in the browser |

## How a pass flows

```
JD + notes → core skill, must-haves, client rules
→ pipeline (all stages + every inflow field)
→ candidates: inflow → new sign-ups → pool → other pipelines
→ location (cheap, first) → seniority / core skill → identity → GitHub (finalists)
→ rank by core skill → JD-fit tables + side-by-side + rejects + team message
→ a human decides → ATS write (read the field first, write the full list)
```

## Principles baked in
- **Core skill before boxes.** Relaxing "1–2 of 3 criteria" relaxes years / brand / title — never the core skill of the job.
- **Judge the role, not the logo.** Corporate IT at a crypto company ≠ production security.
- **Verify before presenting.** Spot-check one key claim per pick; agents overstate.
- **Read-only by default.** No ATS writes without explicit human approval.
- **Humans check LinkedIn.** Finalists only, in their own browser.
- **Binary marks:** every JD row is ✅ meets or ❌ does not meet (not shown = ❌), with the proof next to it.
- **Minimum years is a hard rule** (full-time only).
- Quality scores ≈ 80% signal; salary range = self-assessment (use the lower bound); portal default ranges aren't asks.

See [`lessons-from-runs.md`](skills/stt-match-job/references/lessons-from-runs.md) for the mistakes these rules come from.

## Setup
1. Copy the folders in `skills/` into your project's `.claude/skills/`.
2. Fill in [`stt-config.md`](skills/stt-match-job/references/stt-config.md) (ATS IDs, paths) and [`client-rules.md`](skills/stt-match-job/references/client-rules.md). **Keep your filled-in copies private** — they hold client and candidate data.
3. Requirements: an ATS connection Claude can read (e.g. Airtable MCP), [`gh`](https://cli.github.com/) logged in, `curl`, `pdftotext` (poppler-utils), Python 3.
4. Ask Claude: *"run matchmaking for <job title> at <client>"*, or *"check this candidate's GitHub for Go"*.

## Status
Draft v0.1. The GitHub scan is tested on real profiles; the full pass is being trialled on live jobs. Feedback and ideas welcome.

## Ideas / roadmap
- Auto-reject pre-filter for self-applications that fail hard location / timezone rules.
- A shared "core skill" library per role type (security, Go backend, mobile, DevRel…).
- "No strong inflow for N days" alert per priority job.
