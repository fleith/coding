"""Draw a linked list as connected ASCII nodes.

Usage:
    python scripts/draw_linked_list.py 1 2 3
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.data_structures.linked_list import LinkedList


def draw_linked_list(linked_list: LinkedList) -> str:
    """Return an ASCII representation of the linked list."""
    current = linked_list.head
    if current is None:
        return "[HEAD] -> None"

    parts: list[str] = ["[HEAD] -> "]
    while current is not None:
        parts.append(f"[ {current.data} ]")
        current = current.next
        parts.append(" -> " if current is not None else " -> None")
    return "".join(parts)


def draw_linked_list_gui(linked_list: LinkedList) -> None:
    """Render the linked list in a tkinter window."""
    try:
        import tkinter as tk
    except ImportError as exc:
        raise RuntimeError("tkinter is not available in this Python environment.") from exc

    node_values = linked_list.display()

    root = tk.Tk()
    root.title("Linked List Viewer")

    if not node_values:
        label = tk.Label(root, text="HEAD -> None", font=("Consolas", 16))
        label.pack(padx=20, pady=20)
        root.mainloop()
        return

    node_width = 90
    node_height = 50
    gap = 40
    left_padding = 30
    top_padding = 60

    width = left_padding * 2 + len(node_values) * node_width + (len(node_values) - 1) * gap + 80
    height = 170

    canvas = tk.Canvas(root, width=width, height=height, bg="white")
    canvas.pack()

    canvas.create_text(20, top_padding + node_height // 2, text="HEAD", anchor="w", font=("Consolas", 12, "bold"))
    canvas.create_line(65, top_padding + node_height // 2, left_padding, top_padding + node_height // 2, arrow=tk.LAST, width=2)

    x = left_padding
    y = top_padding
    for i, value in enumerate(node_values):
        canvas.create_rectangle(x, y, x + node_width, y + node_height, outline="black", width=2)
        canvas.create_text(
            x + node_width / 2,
            y + node_height / 2,
            text=str(value),
            font=("Consolas", 12),
        )

        start_x = x + node_width
        end_x = start_x + gap
        mid_y = y + node_height / 2

        if i < len(node_values) - 1:
            canvas.create_line(start_x, mid_y, end_x, mid_y, arrow=tk.LAST, width=2)
        else:
            canvas.create_line(start_x, mid_y, end_x, mid_y, arrow=tk.LAST, width=2)
            canvas.create_text(end_x + 8, mid_y, text="None", anchor="w", font=("Consolas", 12))

        x += node_width + gap

    root.mainloop()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Draw a linked list as connected nodes."
    )
    parser.add_argument(
        "values",
        nargs="*",
        help="Node values in order (default: 1 2 3 4).",
    )
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Render the linked list in a GUI window (tkinter).",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    values = args.values or ["1", "2", "3", "4"]

    linked_list = LinkedList()
    for value in values:
        linked_list.append(value)

    if args.gui:
        draw_linked_list_gui(linked_list)
    else:
        print(draw_linked_list(linked_list))


if __name__ == "__main__":
    main()
