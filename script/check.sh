#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$PROJECT_ROOT"

mkdir -p logs

echo "Running Python quality checks..."
python -m pytest -v 2>&1 | tee logs/test.log

echo "All quality checks passed."
