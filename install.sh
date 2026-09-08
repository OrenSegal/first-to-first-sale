#!/usr/bin/env bash
set -euo pipefail

# Install the signal-outreach skill into ~/.agents/skills/
# Usage: ./install.sh

SKILLS_DIR="${HOME}/.agents/skills"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing signal-outreach..."

mkdir -p "${SKILLS_DIR}/signal-outreach"
cp -r "${SCRIPT_DIR}/signal-outreach/"* "${SKILLS_DIR}/signal-outreach/"

echo "Installed: ${SKILLS_DIR}/signal-outreach/"
echo ""
echo "Available in Claude Code and OpenCode. Pair it with signal-scout"
echo "(https://github.com/OrenSegal/signal-scout) for the research step."
