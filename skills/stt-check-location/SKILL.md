---
name: stt-check-location
description: Check whether a Superteam Talent candidate's location, timezone and nationality fit a job's rules, and widen the search region step by step when the preferred region has no fits. Use this whenever matchmaking or inflow review needs a location/timezone/nationality call — e.g. "is he in the right timezone", "can this client hire her", "anyone in SEA for this role", "expand to Europe", country-ban lists, relocation questions — and as step 1 of stt-match-job.
---

# STT Check: Location

Location is the cheapest filter, so it runs first. But it is also where good people get thrown out by a lazy rule ("lives in Europe" when the client said "Europe preferred"), so separate **hard rules** from **preferences**.

## 1. Classify the job's rule
From the ATS (Preferred Location, timezone field, Notes) and `../stt-match-job/references/client-rules.md`:
- **Hard legal rule** (cannot hire): e.g. a government country list → nationality, not just city.
- **Hard practical rule:** a stated timezone window (e.g. UTC+5 to +10), "US only", on-site city.
- **Preference:** "Europe preferred", "SG/KL strongly preferred", "Asia". Fails here are 🟡, not ❌.

## 2. Find the candidate's real location
Use all of: Airtable Location + Timezone, CV header (address, phone country code), current employer's office, school, languages.
- If they disagree (CV says Lagos, platform says Abu Dhabi), mark **?** and say which sources disagree. It is also an identity signal — pass it to `stt-check-identity`.
- Nationality for legal rules: phone code, school country, native language. If still unclear → **?** and "confirm passport".

## 3. Score
| Result | When |
| --- | --- |
| ✅ | Inside the hard rule and the preference |
| 🟡 | Inside hard rules, outside the preference; or within ~1 hour of a timezone window (say so — clients sometimes flex, e.g. a Singapore candidate interviewing for a UTC+5 limit) |
| ❌ | Breaks a hard rule (banned nationality, outside a strict window by >1–2 h, not in a required country) |
| ? | Location or nationality unknown or conflicting |

Relocation: count "open to relocate" only if the client allows relocation; note visa risk.

## 4. Widen when the preferred region is empty
If no strong candidate passes in the preferred region, widen in rings and **say which ring each pick came from**:
- Example (Asia role): SG/KL → wider SEA → South Asia / East Asia inside UTC+5..+10 → (ask the user before going outside the window).
- Example (US role): SF/NYC/Miami → rest of US → US-relocation candidates.
- Example (Europe-preferred role): Europe → North America.
Don't silently drop the rule: a pick from an outer ring is presented with that 🟡 and a one-line question for the client ("would they take UTC+1?").

## Output
One row for the JD-fit table: `| Location / timezone (<rule>) | <city, country, UTC±x; sources> | ✅/🟡/❌/? |` plus, for legal rules, a nationality row.
