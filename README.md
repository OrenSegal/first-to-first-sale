# first-to-first-sale

[![CI](https://github.com/OrenSegal/first-to-first-sale/actions/workflows/ci.yml/badge.svg)](https://github.com/OrenSegal/first-to-first-sale/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-black)](LICENSE)

`signal-outreach`: a Claude Code / agent-skills skill that turns a
[signal-scout](https://github.com/OrenSegal/signal-scout) prospect list into
the right next action per prospect. Never sends anything automatically.

## What it does

signal-scout finds and scores prospects. It doesn't write the outreach.
signal-outreach takes that report and produces a ready-to-execute next
action, classified by prospect type:

- **Individual**: a 4-touch outreach sequence (first touch, 2 follow-ups,
  breakup), with A/B variants and channel-specific formatting.
- **Segment**: a content/GTM brief staged across the buyer journey, with
  target keywords and channel plans. No message, no opener. An audience
  isn't reachable the way a person is.
- **Company**: a single specific ask under 90 words, an honest execution
  path, and a public-only contact path.

Every item references a specific public signal from the source report. No
cold generic outreach.

## Install

```bash
./install.sh
```

Copies the skill to `~/.agents/skills/signal-outreach`, available in any
Claude Code or OpenCode project.

Manual install:

```bash
cp -r signal-outreach ~/.agents/skills/signal-outreach
```

## Usage

```
/signal-outreach outputs/signal-scout-report.html
```

With a channel focus:

```
/signal-outreach --mode channel-focus --channel email prospects.json
```

**Modes:** quick (first-touch only) · standard (full sequences, briefs, and
pitches, default) · deep (adds A/B variants and response playbooks) ·
channel-focus (Individuals only, one channel)

## Standalone use

The report generator has zero external dependencies (Python 3.10+ stdlib
only):

```bash
python3 signal-outreach/scripts/generate_outreach.py outreach-package.json outputs/signal-outreach-report.html
```

See `examples/outreach-package.json` and its rendered
`examples/outreach-report.html` for the expected input/output shape.

## JSON schema

See [signal-outreach/SKILL.md](signal-outreach/SKILL.md) for the full JSON
schema (`sequences` / `segment_briefs` / `company_pitches`).

## Architecture

```
signal-scout report ──→ signal-outreach ──→ outreach-package.json ──→ signal-outreach-report.html
```

## Dependencies

- Python 3.10+ (stdlib only, no pip install required)
- Claude Code or OpenCode with web search and web fetch tools available

## License

MIT. See `LICENSE`.
