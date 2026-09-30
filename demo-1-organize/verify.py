#!/usr/bin/env python3
"""Check the result of demo 1 independently of the agent.

Passes when every original file still exists exactly once, with the same name
and the same content, nothing was deleted, and no loose files remain in the root.
"""
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "downloads-demo"
MANIFEST = HERE / "manifest.json"
IGNORED = {".DS_Store"}


def main():
    expected = json.loads(MANIFEST.read_text(encoding="utf-8"))
    found = {}
    counts = Counter()
    for path in TARGET.rglob("*"):
        if path.is_file() and path.name not in IGNORED:
            found.setdefault(path.name, []).append(path)
            counts[path.name] += 1

    problems = []
    for item in expected:
        paths = found.get(item["name"], [])
        if not paths:
            problems.append(f"FALTA: {item['name']}")
        elif len(paths) > 1:
            problems.append(f"REPETIDO: {item['name']}")
        elif hashlib.sha256(paths[0].read_bytes()).hexdigest() != item["sha256"]:
            problems.append(f"CONTENIDO DISTINTO: {item['name']}")

    expected_names = {item["name"] for item in expected}
    for name in found:
        if name not in expected_names:
            problems.append(f"NUEVO O RENOMBRADO: {name}")

    loose = [p.name for p in TARGET.iterdir() if p.is_file() and p.name not in IGNORED]
    folders = sorted(p.name for p in TARGET.iterdir() if p.is_dir())

    total = sum(counts.values())
    print(f"Archivos: {total} de {len(expected)}")
    print(f"Subcarpetas ({len(folders)}): {', '.join(folders) if folders else 'ninguna'}")
    print(f"Sueltos en la raíz: {len(loose)}")
    for line in problems:
        print(line)
    ok = not problems and not loose and folders
    print("RESULTADO: OK" if ok else "RESULTADO: REVISAR")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
