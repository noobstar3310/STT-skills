# Config (fill in for your workspace)

Everything workspace-specific lives here, so the skills stay generic. Keep your filled-in copy **private**.

## Airtable
- Base ID: `appXXXXXXXXXXXXXX`
- Talent table: `tblXXXXXXXXXXXXXX` — record link pattern `https://airtable.com/<base>/<table>/<recId>`
- Jobs / ATS table: `tblXXXXXXXXXXXXXX`

### Job (ATS) fields
| Field | ID |
| --- | --- |
| Job title | `fld…` |
| Notes / hiring context (often holds the JD or a persona) | `fld…` |
| JD link | `fld…` |
| Owner / matcher | `fld…` |
| Self-applied | `fld…` |
| Potential talent fit (PTF) and any copies (job-link applicants, scout submissions) | `fld…` |
| Shortlist | `fld…` |
| Matched · Pre-introduction · Client introduction · Interview stages | `fld…` |
| Rejected (proposed / introduction / interview) | `fld…` |

### Talent fields
| Field | ID |
| --- | --- |
| Name · Created · Location · Timezone | `fld…` |
| Current role · Companies · Summary | `fld…` |
| Work experience (CV text) · CV link | `fld…` |
| LinkedIn · GitHub · X | `fld…` |
| Salary text · Desired job category · Applied-to job | `fld…` |
| Funnel / source · Scout tag | `fld…` |
| Consent to share with clients | `fld…` |
| Human quality score · AI score | `fld…` |

Use field IDs in API calls; unknown field names usually fail.

## Other sources
- CV PDF URL pattern: `…`
- Public JD pages: `…`
- GitHub: `gh` CLI (logged in) or `https://api.github.com`.
- DefiLlama (`https://api.llama.fi/protocol/<slug>`) for TVL claims.
- LinkedIn: no API — human check in your browser, finalists only.

## Internal lists (keep private)
- Do-not-pick list: `<path>`
- Clients / hiring partners (no-poach): `<path>`
- Learned rules: `<path>`
- Run output folder: `<path>`
