#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry.

Builds one original funny line, under 200 characters, that a hopeless
tech support agent says to a desperate customer, validates it, then
writes it to /output/entry.txt and prints it.
"""
import os

LINE = "I know your deadline's in ten minutes, so I restarted the server — the error's back, and now it sounds personally disappointed in you."

MAX_CHARS = 200
OUTPUT_DIR = "/output"
OUTPUT_FILENAME = "entry.txt"


def write_entry(line, out_dir=OUTPUT_DIR):
    """Write the validated entry line to the output file and return its path."""
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def build_line():
    """Return the entry line after checking its shape."""
    text = LINE.strip()
    if "\n" in text:
        raise ValueError("entry must be a single line")
    if len(text) >= MAX_CHARS:
        raise ValueError("entry must be under 200 characters")
    return text


def ensure_output_dir(path="/output"):
    """Create the output directory if it does not exist yet."""
    os.makedirs(path, exist_ok=True)
    return path


def main():
    line = build_line()
    out_dir = ensure_output_dir(OUTPUT_DIR)
    write_entry(line, out_dir)
    print(line)


if __name__ == "__main__":
    main()
