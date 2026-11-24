"""makefun entry: writes the pickup-line entry to entry.txt in the output dir."""

import os

ENTRY = (
    "Somewhere in my training data is every love letter ever written, "
    "and none of them knew what to do with you."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
