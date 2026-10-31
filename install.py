#!/usr/bin/env python3
"""Install the bundled skill locally; no network or third-party packages needed."""
import argparse
from datetime import datetime
import os
from pathlib import Path
import shutil
import sys
import tempfile

from tools.verify_bundle import DEFAULT_SKILL, verify


def install(parent, replace=False):
    source = DEFAULT_SKILL.resolve()
    parent = Path(parent).expanduser().resolve()
    destination = parent / "dku-robomaster"
    if (destination == source or destination.is_relative_to(source)
            or source.is_relative_to(destination)):
        raise ValueError("Installation destination overlaps the repository skill")
    if destination.is_symlink():
        raise ValueError("Destination is a symbolic link; select another destination")
    if destination.exists() and (not destination.is_dir() or not replace):
        raise ValueError("Destination exists; use --replace to preserve a backup and update it")
    verify(source)
    parent.mkdir(parents=True, exist_ok=True)
    backup = None
    with tempfile.TemporaryDirectory(prefix=".dku-install-", dir=parent) as temp:
        staged = Path(temp) / "skill"
        shutil.copytree(source, staged, ignore=shutil.ignore_patterns(".DS_Store", "__pycache__", "*.pyc"))
        verify(staged)
        if destination.exists():
            backups = parent.parent / "skill-backups"
            backups.mkdir(parents=True, exist_ok=True)
            stamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
            backup = backups / ("dku-robomaster-" + stamp)
            destination.rename(backup)
        try:
            os.replace(staged, destination)
        except OSError:
            if backup is not None and not destination.exists():
                backup.rename(destination)
            raise
    return destination, backup


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app", choices=("codex", "claude"), default="codex")
    parser.add_argument("--destination", type=Path, help="Custom parent skills directory")
    parser.add_argument("--replace", action="store_true", help="Back up an existing skill before updating")
    args = parser.parse_args()
    parent = args.destination or Path.home() / (".agents" if args.app == "codex" else ".claude") / "skills"
    try:
        destination, backup = install(parent, replace=args.replace)
        print("Installed: " + str(destination))
        if backup:
            print("Previous copy retained: " + str(backup))
        print("Open a new conversation or refresh the skill list; invoke dku-robomaster.")
        return 0
    except (OSError, ValueError, KeyError, TypeError, SyntaxError) as error:
        print("Installation failed: " + str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
