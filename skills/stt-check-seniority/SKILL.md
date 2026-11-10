---
name: stt-check-seniority
description: Judge a Superteam Talent candidate's real seniority and whether they have the job's core skill, from CV dates and actual responsibilities rather than titles, logos or the "years" field. Use this whenever matchmaking needs a call on years of experience, level (IC / lead / head), "is this the right kind of engineer", corporate vs production work, salary-vs-level sense checks, or relaxed criteria ("1–2 of 3 boxes") — and as step 2 of stt-match-job.
---

# STT Check: Seniority + core skill

Most wrong picks pass on paper: right years, right logo, wrong job. This check reads what the person actually did.

## 1. Name the core skill first
Write one line: the thing the role exists to do (from `stt-match-job` step 1). Examples:
- Head of Security at a developer platform → "secures internet-facing production infrastructure (cloud, bare metal), leads incidents".
- Senior Engineer at a Go startup → "builds Go backend services in production".
- Consumer-app Product Engineer → "ships a consumer mobile app end to end (React Native)".

## 2. Read the CV, not the summary
Get the CV text (Work Experience field, or `../stt-match-job/scripts/fetch_cv.sh`). For each job: dates, employer, title, and **what they owned** (verbs + objects).
- **Real years** = sum of full-time CV dates for relevant work. Internships, bootcamps, ambassador and "fellow" roles count separately. The Airtable `years` field is often wrong.
- **Level:** IC / tech lead (projects) / manager (people, hiring, budget) / head (strategy, roadmap, owns a function). A "Lead" title at a 3-person agency ≠ lead at a scale-up.
- **Scope test:** is the work on the **product customers use** (production systems, the shipped app, protocol code) or on **internal/company systems** (staff laptops, SSO, office network, internal tools)? Same words ("security", "infrastructure", "platform") mean different jobs.
- **Language test:** is the required language the main one, or one of four listed? One line under one job ≠ main language.

## 3. Score the core skill
| | Means |
| --- | --- |
| ✅ | Did the core skill as their main job, for the required years, with outcomes (numbers, systems named) |
| 🟡 | Did it partly, briefly, as a secondary skill, or on internal rather than production systems |
| ❌ | Not shown |

A ❌ on the core skill removes the candidate, however many other boxes they tick — even when the user has relaxed the criteria. Relaxing "1–2 of 3 boxes" relaxes the boxes (years, brand, title), not the core skill. If no one passes, say so and suggest targeted sourcing rather than lowering the core.

## 4. Other signals
- **Brand:** judge the role, not the logo (see `../stt-check-identity/fraud-signals.md` for tiers and look-alikes: "Phantom" agency ≠ Phantom wallet).
- **Stability:** more than one stint under ~12 months (self-employed included) = orange flag; note the reason if given.
- **Salary vs level:** ask far below the claimed level (offshore pattern) or far above a thin profile → flag. Wide range → use the lower bound; portal default range → "no real ask".
- **H ⭐:** ~80% reliable. If your read disagrees by ≥2 stars, say why.

## Output
JD-fit rows: core skill, years, level/leadership, each must-have, stability — each with concrete proof (employer, dates, what they owned) and ✅/🟡/❌/?.
