#!/bin/bash
set -euo pipefail

echo "== docs/source/scrape.py =="
nl -ba docs/source/scrape.py

echo
echo "== locate HTMLSession close definition and get usage =="
rg -n "class HTMLSession|def close|def get\\(" requests_html.py docs/source -n
