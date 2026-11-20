"""Offline syntax, notebook output, link, and selected credential checks.

Uses only the standard library. Never prints matching credential values.
Does not execute Spark or contact cloud services.
"""

from __future__ import annotations

import ast
import json
from pathlib import Path
import re
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKIP_PARTS = {".git", ".venv", "venv", "__pycache__", "private"}
PATTERNS = {
    "signed URL signature": re.compile(r"[?&]sig=[A-Za-z0-9%+/=]{12,}"),
    "Databricks token": re.compile(r"\bdapi[a-fA-F0-9]{20,}\b"),
    "GitHub token": re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    "storage connection-string key": re.compile(r"AccountKey=[A-Za-z0-9+/=]{24,}"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}


def check() -> list[str]:
    problems: list[str] = []
    notebooks = 0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.relative_to(ROOT).parts):
            continue
        if path.suffix.lower() not in {".ipynb", ".py", ".md", ".json", ".yml", ".yaml", ".sql"}:
            continue
        relative = path.relative_to(ROOT).as_posix()
        text = path.read_text(encoding="utf-8-sig")
        for label, pattern in PATTERNS.items():
            if pattern.search(text):
                problems.append(f"{relative}: possible {label}; inspect privately")
        if path.suffix == ".ipynb":
            notebooks += 1
            try:
                notebook = json.loads(text)
                if notebook.get("nbformat") != 4:
                    problems.append(f"{relative}: expected notebook format 4")
                for index, cell in enumerate(notebook["cells"], 1):
                    if cell["cell_type"] != "code":
                        continue
                    if cell.get("outputs") or cell.get("execution_count") is not None:
                        problems.append(f"{relative}: cell {index} contains outputs or execution state")
                    source = re.sub(r"^%python\s*\n", "", "".join(cell["source"]))
                    try:
                        ast.parse(source)
                    except SyntaxError:
                        problems.append(f"{relative}: cell {index} has unsupported magic or invalid Python syntax")
            except (ValueError, KeyError, TypeError):
                problems.append(f"{relative}: invalid notebook structure")
        elif path.suffix == ".json":
            try:
                json.loads(text)
            except ValueError:
                problems.append(f"{relative}: invalid JSON")
        elif path.suffix == ".py":
            try:
                ast.parse(text)
            except SyntaxError:
                problems.append(f"{relative}: invalid Python syntax")
        elif path.suffix == ".md":
            prose = re.sub(r"```.*?```", "", text, flags=re.S)
            for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", prose):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                destination = unquote(target.split("#", 1)[0].split("?", 1)[0])
                if destination and not (path.parent / destination).exists():
                    problems.append(f"{relative}: missing local link {destination}")
    if notebooks == 0:
        problems.append("No notebooks found")
    return problems


if __name__ == "__main__":
    failures = check()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        raise SystemExit(1)
    print("PASS: notebook syntax, clean outputs, local links, and selected credential patterns")
