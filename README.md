# Unison Infrastructure

Reproducible development, integration, lab, deployment, and observability
profiles for Unison. This repository describes machines and environments; it
does not own application contracts or personal data.

## Current environments

| Profile | State | Purpose |
| --- | --- | --- |
| `dev-windows-control` | active | Codex/human control plane and remote coordination |
| `dev-nuc` | active | Ubuntu builds, tests, and integration |
| `gpu-lab` | deferred | Inference deployment and hardware qualification after inventory |

Start with `AGENTS.md`, then validate profile files against
`schemas/environment-profile.schema.json` by running `python scripts/validate.py`.
CI runs the same command. No secrets or private network
credentials belong here.

License: Apache-2.0 for software and documentation committed here unless a file
states otherwise.
