---
name: stt-check-identity
description: Screen a Superteam Talent candidate for fraud and identity problems — overlapping jobs, history that doesn't add up, handle/name mismatches, North Korean-style scam patterns, do-not-pick list, no-poach — and produce a LinkedIn/X checklist for a human to verify in the browser. Use this whenever the user asks "is this person real", "fraud check", "verify identity", "any red flags", mentions no LinkedIn / suspicious CV / random endorsements, or before any candidate is shortlisted (step 3 of stt-match-job). Hackers pose as candidates to reach clients; one fake intro can lose a client.
---

# STT Check: Identity + fraud

Fraud profiles are built to look like ⭐4–5, so this runs **before** trusting a star or a logo. It never needs to prove fraud — it decides how much checking a human must do before an intro.

## 1. Internal lists (hard stops)
- Do-not-pick list (path in `../stt-match-job/references/stt-config.md`) → exclude.
- Status = Fraud, or a Fraud / Potential Fraud badge → exclude, or ask your recruiting lead.
- Currently employed at an STT hiring partner → exclude (no-poach), even if they applied themselves.

## 2. Count the tells
Use the full list in `fraud-signals.md` (next to this file). The ones that keep showing up:
- **Overlapping "current" jobs**, especially unrelated ones (Senior Director + substitute teacher + own firm).
- **Copy-pasted bullets** between different roles; template or AI text; a CV written for another employer.
- **Handle/email ≠ name** on GitHub, X, Telegram, email.
- **Geography doesn't fit:** name, school, phone code and city point to different countries; platform location ≠ CV location.
- **History doesn't fit:** GitHub/X account newer than claimed experience; years claimed > CV dates; credentials impossible for the tenure.
- **Too broad / too good:** 6+ chains, 30+ skills, round huge numbers, every job a top brand and all remote.
- **Pay:** very low ask for the claimed seniority, or an extreme ask on a thin profile.
- **Short stints:** more than one under ~12 months (self-employed included) → orange (stability, and a common fraud pattern).
- **Missing trail:** no LinkedIn at all, no photo anywhere, no dates on the CV. Not fraud by itself (some real engineers avoid social media) — but it moves the person to "verify on video first".

Not trust signals on their own: Superteam membership, hackathon participation, a polished CV (all seen on confirmed frauds).

Scoring: 0–1 tells → **low** · 2–3 → **medium** · 4+, or any hard tell (someone else's CV, placeholder phone, Fraud status) → **high**.

## 3. Counter-evidence
Strong real-person proof lowers risk: long-lived GitHub with merged PRs in real orgs that match the CV; named in signed audit reports or company blog posts; consistent phone/school/city; a public talk or article under their name.

## 4. Human checklist (LinkedIn / X) — finalists only
The agent can't open LinkedIn. Give the user a short list to check in their own browser (a few profiles, never bulk — bulk visits get the account flagged):
- LinkedIn "About this profile": account creation date (new = red, even under a year), verification (gov-ID = green).
- Real activity: posts and comments over time (reactions don't count); connection count.
- **Skill endorsements:** random or unrelated endorsers = scam signal.
- History matches the CV (employers, dates, titles).
- X: account age vs claimed career, organic engagement.
- Photo: reverse image search if it looks generated.
If the person has no LinkedIn, recommend a **video coffee chat with cameras on** before any intro.

## Output
JD-fit rows: `| Fraud risk | low/med/high — tells: …; counter-evidence: … | ✅/🟡/❌ |`, `| No-poach / DO-NOT-PICK | … |`, plus the human checklist when risk ≥ medium or there is no LinkedIn. If risk is high, say "flag to the recruiting lead + Potential Fraud badge" — leave the final Fraud call to the lead.
