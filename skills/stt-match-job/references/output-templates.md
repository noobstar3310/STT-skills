# Output templates

Picks are never bullets only — every suggested candidate gets a JD-fit table. Keep words simple; the reader decides in a minute.

## Run file header
```
# <Client>: <Role> — matchmaking (<YYYY-MM-DD>)
- ATS: `<recId>` · status · Read-only run; nothing written.
- Core skill: <one line>
- Must-haves: … · Nice-to-haves: … · Client rules: location/timezone, budget, nationality
- Pipeline: <stage: names> (inflow fields empty / not)
- Searched: <table: source | count | result>
```

## Per pick
```
### <Rank>. <Name> (<City>) — <Shortlist | PTF | Ask>
[Airtable](<record link>) · `<rec>` · LinkedIn · GitHub · CV
Ask <salary or "no real ask"> · Consent <✅/❌> · H ⭐<n> · Stage on this job: <none/…>

| Requirement | Proof | |
| --- | --- | --- |
| <core skill> | <concrete evidence: employer, dates, repo/PR link> | ✅/🟡/❌/? |
| <each must-have> | … | |
| <each nice-to-have> | … | |
| <client rule: location/timezone> | … | |
| <client rule: budget> | … | |
| No-poach / DO-NOT-PICK | … | |
| Stability (short stints) | … | |
| Fraud risk | low/med/high + why | |
| Consent | … | |

**✅ a · 🟡 b · ❌ c · ? d.** Why: <one line>. Watch-out: <one line>.
```

## Side-by-side
```
| Requirement | <A> | <B> | <C> |
| --- | --- | --- | --- |
| <core skill> | ✅ | 🟡 | ❌ |
| … | | | |
| **✅ count** | **n** | **n** | **n** |
```
Then one line on ranking if it differs from the ✅ count.

## Rejects
`| Name | Record | Why not (one line) |`

## Inflow dates table (inflow runs)
`| Name | Job | Profile created (MYT) | Applied to | Funnel / scout | Where on the job | Verdict |`

## Telegram (Fulfillment Operations) — hold until the user asks
```
Match Making (added to shortlisted)

<Job title> - <Company>
- <Name>

Match Making (added to potential talent fit)

<Job title> - <Company>
- <Name>
```
Internal group only; never put candidate names in public posts. Never name a confidential role outside internal channels.
