#!/usr/bin/env python3
"""Validate and format JSON files passed as CLI args."""

from __future__ import annotations

import json
import sys
from pathlib import Path

REQUIRED_FIELDS = ("name", "description", "tags", "export")
SENTIO_PARENTS = frozenset(("Sentio/Visuals", "Sentio/Dashboards"))


def get_json_files_from_args(argv: list[str]) -> list[Path]:
    """Filter CLI args to existing .json files."""
    files = [Path(item) for item in argv]
    return [path for path in files if path.suffix == ".json" and path.exists()]


def _validate_sentio_metadata(data: list[dict], path: Path) -> list[str]:
    """Return a list of error strings for missing required fields."""
    errors: list[str] = []
    for idx, obj in enumerate(data):
        missing = [f for f in REQUIRED_FIELDS if f not in obj]
        if missing:
            errors.append(
                f"{path}[{idx}]: missing required field(s): {', '.join(missing)}"
            )
    return errors


def _is_sentio_parent(path_str: str) -> bool:
    """Check if the path lives inside a Sentio/Visuals or Sentio/Dashboards dir."""
    norm = path_str.replace("\\", "/").lstrip("/").rstrip("/")
    depth = len(norm.split("/"))
    # Need at least Sentio/{Folder}/filename
    if depth < 3:
        return False
    candidate = "/".join(norm.split("/", 2)[-2].split("/")[:2])
    return candidate in SENTIO_PARENTS


def format_and_validate_json_file(path: Path) -> tuple[bool, str]:
    """Validate and format one JSON file."""
    try:
        raw = path.read_text(encoding="utf-8")
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        return False, f"{path}: invalid JSON ({exc})"

    # Strict validation for Sentio metadata files
    if _is_sentio_parent(str(path)) and isinstance(parsed, list):
        errors = _validate_sentio_metadata(parsed, path)
        if errors:
            return False, "; ".join(errors)

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
