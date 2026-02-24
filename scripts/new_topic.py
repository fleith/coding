"""Generate source and test stubs for new study topics.

Examples:
    python scripts/new_topic.py --type algorithm --category sorting --name selection_sort
    python scripts/new_topic.py --type data-structure --category tree --name binary_search_tree
"""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a source file and matching test stub."
    )
    parser.add_argument(
        "--type",
        choices=["algorithm", "data-structure"],
        required=True,
        help="Topic type to generate.",
    )
    parser.add_argument(
        "--category",
        required=True,
        help="Category folder inside src/tests (e.g., sorting, tree, graph).",
    )
    parser.add_argument(
        "--name",
        required=True,
        help="Module/function name in snake_case (e.g., selection_sort).",
    )
    return parser.parse_args()


def write_new_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    path.write_text(content, encoding="utf-8")


def source_template(module_name: str) -> str:
    return f'''"""TODO: Implement {module_name}.

Complexity:
    Time: TODO
    Space: TODO
"""


def {module_name}(values):
    """Return a result for the given values."""
    raise NotImplementedError("Implement this function")
'''


def test_template(import_path: str, module_name: str) -> str:
    return f"""from {import_path} import {module_name}


def test_{module_name}_empty():
    # Replace with real expected behavior.
    assert True


def test_{module_name}_single():
    # Replace with real expected behavior.
    assert True


def test_{module_name}_general():
    # Replace with real expected behavior.
    assert True
"""


def main() -> None:
    args = parse_args()
    base = "algorithms" if args.type == "algorithm" else "data_structures"

    source_path = Path("src") / base / args.category / f"{args.name}.py"
    test_path = Path("tests") / base / args.category / f"test_{args.name}.py"
    import_path = str(source_path.with_suffix("")).replace("\\", ".").replace("/", ".")

    write_new_file(source_path, source_template(args.name))
    write_new_file(test_path, test_template(import_path, args.name))

    print(f"Created: {source_path}")
    print(f"Created: {test_path}")


if __name__ == "__main__":
    main()
