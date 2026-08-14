# Agent guide

Read `README.md` and the selected file under `environments/` before acting.

- Never commit secrets, Tailscale keys, private addresses, or credential files.
- Treat Windows as the control plane and Ubuntu as the canonical runtime path.
- Do not claim GPU, energy, thermal, RF, or physical qualification without an
  inventory-bound run and evidence artifact.
- Keep profiles declarative, versioned, non-interactive, and recoverable.
- Preserve existing machine state; use clean worktrees and explicit targets.
- Record exact commands, revisions, environment, evidence class, and rollback.
