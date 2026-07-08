from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

REQUIRED_SECTIONS = [
    "适用场景",
    "不适用场景",
    "工作流",
]


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    block = text[4:end]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"')
    return data


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        return [f"{path.name}: missing SKILL.md"]

    readme_md = path / "README.md"
    if not readme_md.exists():
        errors.append(f"{path.name}: missing README.md")

    text = skill_md.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)
    name = meta.get("name")
    description = meta.get("description")

    if not name:
        errors.append(f"{path.name}: missing frontmatter name")
    elif name != path.name:
        errors.append(f"{path.name}: frontmatter name should match directory name")

    if not description:
        errors.append(f"{path.name}: missing frontmatter description")
    elif len(description) < 40:
        errors.append(f"{path.name}: description is too short to trigger reliably")

    for section in REQUIRED_SECTIONS:
        if not re.search(rf"^##\s+{re.escape(section)}\s*$", text, re.MULTILINE):
            errors.append(f"{path.name}: missing section ## {section}")

    if "验证" not in text and "Verify" not in text:
        errors.append(f"{path.name}: missing verification guidance")

    if "安全" not in text and "边界" not in text and "Safety" not in text:
        errors.append(f"{path.name}: missing safety or boundary guidance")

    return errors


def validate_markdown_links() -> list[str]:
    errors: list[str] = []
    for md_path in sorted(ROOT.rglob("*.md")):
        text = md_path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip()
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
                or "://" in target
            ):
                continue

            link_path = target.split("#", 1)[0]
            if not link_path:
                continue

            resolved = (md_path.parent / link_path).resolve()
            try:
                resolved.relative_to(ROOT)
            except ValueError:
                continue

            if not resolved.exists():
                rel_md = md_path.relative_to(ROOT)
                errors.append(f"{rel_md}: broken local link {target}")

    return errors


def main() -> int:
    if not SKILLS_DIR.exists():
        print("skills directory not found", file=sys.stderr)
        return 2

    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    all_errors: list[str] = []
    for path in skill_dirs:
        all_errors.extend(validate_skill(path))
    all_errors.extend(validate_markdown_links())

    if all_errors:
        print("Skill validation failed:")
        for error in all_errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skills.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
