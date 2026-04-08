#!/usr/bin/env python3
"""Validate and format JSON files passed as CLI args."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def get_json_files_from_args(argv: list[str]) -> list[Path]:
    """Filter CLI args to existing .json files."""
    files = [Path(item) for item in argv]
    return [path for path in files if path.suffix == ".json" and path.exists()]


def format_and_validate_json_file(path: Path) -> tuple[bool, str]:
    """Validate and format one JSON file."""
    try:
        raw = path.read_text(encoding="utf-8")
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        return False, f"{path}: invalid JSON ({exc})"

    formatted = json.dumps(parsed, indent=2, ensure_ascii=False, sort_keys=False) + "\n"
    if formatted != raw:
        path.write_text(formatted, encoding="utf-8")
    return True, ""


def main() -> int:
    json_files = get_json_files_from_args(sys.argv[1:])
    if not json_files:
        print("No changed .json files provided. Skipping.")
        return 0

    failures: list[str] = []
    for json_file in json_files:
        ok, message = format_and_validate_json_file(json_file)
        if not ok:
            failures.append(message)
            print(f"::error file={json_file}::{message}")
        else:
            print(f"Validated and formatted: {json_file}")

    if failures:
        print("\nJSON validation failed. Fix invalid files and push again.")
        return 1

    print("JSON validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
