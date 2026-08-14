#!/usr/bin/env python3
"""Validate every committed environment profile against the canonical schema."""

from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    schema = yaml.safe_load((ROOT / "schemas/environment-profile.schema.json").read_text())
    profiles = sorted((ROOT / "environments").glob("*.yaml"))
    if not profiles:
        raise SystemExit("no environment profiles found")
    for profile in profiles:
        jsonschema.validate(yaml.safe_load(profile.read_text()), schema)
        print(f"validated {profile.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
