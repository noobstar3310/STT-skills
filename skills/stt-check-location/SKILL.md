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
- **Preference:** "Europe preferred", "SG/KL strongly preferred", "Asia". A miss here is ❌ for the preference row, but not a reject on its own — say so.

## 2. Find the candidate's real location
Use all of: Airtable Location + Timezone, CV header (address, phone country code), current employer's office, school, languages.
- If they disagree (CV says Lagos, platform says Abu Dhabi), mark ❌ "not confirmed" and say which sources disagree. It is also an identity signal — pass it to `stt-check-identity`.
- Nationality for legal rules: phone code, school country, native language. If still unclear → ❌ "not confirmed — check passport".

## 3. Score
| Result | When |
| --- | --- |
| ✅ | Meets the rule (inside the window / allowed country). Within ~1 h of a soft timezone limit counts as ✅ only if the client has flexed before — say so |
| ❌ | Does not meet it: outside the window, banned nationality, not in a required country, **or location/nationality unknown or conflicting** (write "not confirmed — ask") |

Use separate rows for the hard rule and the preference, so a preference miss (❌) doesn't hide that the hard rule is met (✅).

Relocation: count "open to relocate" only if the client allows relocation; note visa risk.

## 4. Widen when the preferred region is empty
If no strong candidate passes in the preferred region, widen in rings and **say which ring each pick came from**:
- Example (Asia role): SG/KL → wider SEA → South Asia / East Asia inside UTC+5..+10 → (ask the user before going outside the window).
- Example (US role): SF/NYC/Miami → rest of US → US-relocation candidates.
- Example (Europe-preferred role): Europe → North America.
Don't silently drop the rule: a pick from an outer ring is presented with ❌ on the preference row and a one-line question for the client ("would they take UTC+1?").

## Output
One row for the JD-fit table: `| Location / timezone (<rule>) | <city, country, UTC±x; sources> | ✅/❌ |` plus, for legal rules, a nationality row.
