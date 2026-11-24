from pathlib import Path

def get_target_folder(filename: str, rules: dict[str, list[str]]) -> str:
    extension = Path(filename).suffix.lower()
    for i in rules.keys():
        if extension in rules[i]:
            return i
    return "Other"

def plan_organization(
    folder_path: str, rules: dict[str, list[str]]
) -> list[tuple[Path, Path]]:
    base_dir = Path(folder_path)
    plan: list[tuple[Path, Path]] = []
    for item in base_dir.iterdir():
        if item.is_dir() or item.name.startswith("."):
            continue
        target_folder_name = get_target_folder(item.name, rules)
        destination = base_dir / target_folder_name / item.name
        plan.append((item, destination))
    return plan

def apply_organization(plan: list[tuple[Path, Path]]) -> int:
    moved_count = 0
    for source, destination in plan:
        destination.parent.mkdir(exist_ok=True)
        source.rename(destination)
        moved_count += 1
    return moved_count
