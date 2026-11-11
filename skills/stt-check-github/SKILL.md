---
name: stt-check-github
description: Verify a technical candidate's claimed skills against their public GitHub — account age, own vs forked repos, languages, commit-date spread, merged pull requests in real organisations — and catch padding such as one-day take-home repos, forks-only profiles and tiny PRs. Use this whenever the user asks to "check his GitHub", "prove she has Go/Rust experience", "is this code real", "full gh scan", or when stt-match-job reaches finalists for any engineering, security, DevRel or smart-contract role.
---

# STT Check: GitHub

GitHub is the best public proof for engineers, and the easiest place to be fooled by numbers. "250 KB of Go" can be one afternoon with an AI agent. This check answers one question: **does public code prove the claimed skill, at what depth?**

## 1. Run the scan
```
python3 scripts/github_scan.py <handle> [--lang Go] [--org solana-foundation ...]
```
It needs the `gh` CLI (logged in) and prints: account age and followers; own vs forked repos with language, created/pushed dates, commit count and **how many distinct days the commits span**; merged PR counts per organisation; flags (see below). Find the handle in the candidate record's GitHub field, the CV header, or by searching the name if missing.

## 2. Read the flags (and look yourself)
| Flag | What it usually means | Do |
| --- | --- | --- |
| `ONE-DAY REPO` (many commits, 1–2 days) | Take-home test, hackathon, or AI-generated dump | Open the file list: `Coding_Test*.pdf`, `Instructions.pdf`, `CLAUDE.md`/`agents.md` → coding test. Proves "can ship with AI", not depth |
| `FORKS ONLY` | No own public code | Skill can't be verified → ❌ "not provable on GitHub — ask for samples" |
| `NEW ACCOUNT` (< 1 yr) | Normal for students; a red flag for "10-yr senior" | Pass to stt-check-identity |
| `TINY PRS` (merged PRs mostly < 20 lines) | Docs, typo, dependency bumps | Don't call it deep contribution |
| `NAME MISMATCH` (handle/name unrelated to the person) | Possible borrowed account | Pass to stt-check-identity |

Then open 1–3 of the most relevant items yourself (the biggest merged PR in the target language, the main own repo) and note what they actually are.

## 3. Decide depth
| Level | Evidence |
| --- | --- |
| **Proven deep** → ✅ | Sustained work over months in the target language/stack: many merged PRs in real orgs (e.g. dozens merged in a core protocol repo), or an own project with commits over weeks and real users/stars |
| **Proven used** → ✅ only if the JD asks "has used X"; ❌ if it asks for depth/strength | Real but small: a few merged PRs, short projects, or work that matches the CV but is thin |
| **Not provable** → ❌ | Forks only, private work, no handle — say "private work, ask for samples" (not proof of fraud) |
| **Contradicts CV** → ❌ | Account newer than claimed history, code in a different stack, someone else's code |

Private employer code is normal for senior people — a ❌ here means "not proven yet", not "false"; say that in the proof. A smart-contract role with no GitHub at all is too hard to verify → say so.

## Output
JD-fit row(s): `| <skill> on GitHub | <account since YYYY; N own repos; merged PRs: org/repo ×n (+lines); one-day/forks flags; links> | ✅/❌ |` — always with links to the PRs or repos used as proof.
