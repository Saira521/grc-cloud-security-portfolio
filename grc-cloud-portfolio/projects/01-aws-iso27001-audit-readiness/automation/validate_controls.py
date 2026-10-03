from pathlib import Path
import sys
import yaml

REQUIRED_FIELDS = {
    "id",
    "title",
    "objective",
    "risk_refs",
    "owner",
    "implementation",
    "evidence_sources",
    "test_frequency",
    "automation_level",
    "framework_refs",
}


def main() -> int:
    control_file = Path(__file__).resolve().parents[1] / "controls" / "unified-controls.yaml"
    data = yaml.safe_load(control_file.read_text(encoding="utf-8"))
    controls = data.get("controls", [])

    if not controls:
        print("ERROR: No controls found")
        return 1

    errors = []
    ids = set()

    for index, control in enumerate(controls, start=1):
        missing = REQUIRED_FIELDS - set(control)
        if missing:
            errors.append(f"Control #{index} missing fields: {sorted(missing)}")

        control_id = control.get("id")
        if control_id in ids:
            errors.append(f"Duplicate control id: {control_id}")
        ids.add(control_id)

        if not control.get("risk_refs"):
            errors.append(f"{control_id}: at least one risk reference is required")
        if not control.get("evidence_sources"):
            errors.append(f"{control_id}: at least one evidence source is required")
        if not control.get("owner"):
            errors.append(f"{control_id}: owner is required")

    if errors:
        print("GRC control validation FAILED")
        for error in errors:
            print(f" - {error}")
        return 1

    print(f"GRC control validation PASSED: {len(controls)} controls checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
