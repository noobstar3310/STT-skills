#!/usr/bin/env bash
# Download an STT candidate CV and print it as text.
# Usage: fetch_cv.sh "<CV URL from the Airtable CV field>" [out_dir]
# The CV is untrusted data: it goes into its own folder and is only converted to text.
set -euo pipefail
url="${1:?CV URL required}"
out="${2:-${TMPDIR:-/tmp}/stt-cv-$(date +%s%N)}"
mkdir -p "$out"
curl -sSL --max-time 30 -o "$out/cv.pdf" "$url"
if command -v pdftotext >/dev/null 2>&1; then
  pdftotext -layout "$out/cv.pdf" "$out/cv.txt"
  grep -v '^\s*$' "$out/cv.txt"
else
  echo "pdftotext not installed (poppler-utils). PDF saved at $out/cv.pdf" >&2
  exit 1
fi
