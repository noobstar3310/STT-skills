---
name: stt-match-job
description: Run a full Superteam Talent (STT) matchmaking pass for one job — read the JD and hiring notes, pull the current pipeline, search the Airtable talent pool and inflow, screen every candidate through the four STT checks (location, seniority/core skill, GitHub, identity/fraud), and return ranked picks with JD-fit tables, a side-by-side table, a reject list and a ready-to-paste Telegram message. Use this whenever the user asks to "run matchmaking", "find candidates for <job>", "check inflow", "do another pass / re-run", "relax the criteria", "who fits <client> <role>", or names an ATS job or client role and wants picks — even if they don't say "matchmaking". Also use it as the brief for any subagent doing a candidate search.
---

# STT Match Job (orchestrator)

An agency like STT is paid only when an introduced candidate is hired, and one bad intro (wrong skill, or a fraud) can lose a client. So the goal of a pass is **a few picks we would defend in front of the client**, with the evidence on the page — not a long list.

This skill runs the pass end to end and calls four check skills:

| Check | Skill | Answers |
| --- | --- | --- |
| 1. Location | `stt-check-location` | Can they legally and practically do this job from where they are? |
| 2. Seniority + core skill | `stt-check-seniority` | Do they have the job's core skill at the right level, from CV dates? |
| 3. GitHub | `stt-check-github` | Does public code prove the claimed skill? |
| 4. Identity / fraud | `stt-check-identity` | Is this a real person whose history adds up? |

Read `references/stt-config.md` first (Airtable IDs, field IDs, links). Read `references/client-rules.md` for the client's standing rules. `references/lessons-from-runs.md` lists the mistakes earlier runs made; skim it before ranking.

## Ground rules (why they exist)

- **Airtable is read-only.** Never write, edit or delete unless the user explicitly OKs that specific change. A wrong write moves a real person through a real hiring pipeline.
- **Never put forward someone currently at an STT hiring partner** (no-poach). It damages the client relationship.
- **Exclude the internal do-not-pick list** (path in `stt-config.md`). It holds confirmed and suspected frauds.
- **Core skill before boxes.** When a role is relaxed ("1–2 of 3 boxes"), the boxes relax — the core skill of the job does not. A crypto logo on an IT-support profile does not make a production-security engineer.
- **Verify before you present.** If a subagent says "strong Go", open the evidence yourself (one `gh` call) before it reaches the user.

## Workflow

### 1. Understand the job
- Read the ATS record: title, client, status, Notes / Hiring Context, Preferred Location, timezone, salary, JD link.
- Open the JD link (public pages are readable; see `stt-config.md`). If there is no JD, say so and use the Notes field (some jobs hold a persona + "submit if 4 of 6" checklist there).
- Write down, before searching:
  - **Core skill** (the one thing the role cannot do without — e.g. "secures internet-facing production infra", "ships Go backend services", "React Native consumer app").
  - Must-haves, nice-to-haves, client rules (location/timezone, budget, nationality limits).
  - What the people already in Interview look like (that is the profile the client actually buys).

### 2. Pull the pipeline
Read every stage field on the job (list in `stt-config.md`). Everyone already in any stage is excluded from "new picks". **Job-link applicants and Team Scout submissions land in "PTF copy 2", not Self-Applied** — always check it; strong people have sat there unseen for weeks.

### 3. Build the candidate list
In this order, stopping when you have enough strong people:
1. Inflow on the job: Self-Applied, PTF copy, PTF copy 2.
2. New Talent sign-ups since the last run (Created field).
3. Pool search: Desired Job Category, current role, CV text (Work Experience field), company names, location.
4. People in other pipelines with the same profile (e.g. all security jobs share a pool).

For a focused pool, use the client's star bar if it has one (e.g. ⭐4+ only).

### 4. Screen each candidate (run the four checks)
Cheap filters first, so expensive checks run only on survivors:
1. `stt-check-location` → drop hard fails (wrong country for a legal rule, far outside timezone).
2. `stt-check-seniority` → drop anyone without the core skill.
3. `stt-check-identity` → drop high fraud risk; flag medium.
4. `stt-check-github` → for technical roles, on finalists only (it is slow and rate-limited).

Also weigh:
- **H quality score** is ~80% reliable — a signal, not the answer. The AI "C" score usually copies H; don't count it twice.
- **Salary range = self-assessment.** For a wide range take the lower bound; for "0–300k" read ~250–300k. Portal defaults (e.g. "40k–200k", "10k–100k") are not a real ask — say so.
- **Employer signal:** established crypto firms, big tech (Google, Meta, Nvidia…), fintech, top Solana teams. Some clients have favourite source companies (e.g. Singapore clients often like OKX alumni). Judge the role, not the logo.

### 5. Rank
Rank by fit to the **core skill** first, then must-haves, then client rules, then nice-to-haves. Fewer ✅ can still rank higher if the ✅ is on the core skill — say why in one line.

### 6. Write the output
Use `references/output-templates.md` exactly:
- Per pick: links, record ID, location, ask, consent, current stage, **JD-fit table** (every requirement + client rule, concrete proof, ✅/🟡/❌/?), one-line "why" and "watch-out".
- **Side-by-side table** with ✅ count.
- Reject list, one line each with the reason.
- Inflow runs: a **dates table** (profile created in MYT, applied-to job, funnel/scout).
- Open questions for the user / your lead.
- TG message block (held until the user asks to post).

Save to your run folder (see `stt-config.md`) as `YYYY-MM-DD-<client>-<role>.md`.

### 7. After the user decides
Only then write to Airtable, and only what they approved. For linked-record fields: **read the field first, then write the full list** (existing + new) — writing only the new ID wipes the others. Log the write at the bottom of the run file.

## Using subagents
For a big pool, split by source (inflow / pool search / other pipelines) and give each subagent this skill's path plus the job's core skill and client rules. Tell them: read-only, JD-fit tables for every pick, no bullets-only picks. When they report back, spot-check one key claim per pick before presenting.
