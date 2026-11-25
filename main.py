#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry.

Writes one original funny line, under 200 characters, that a hopeless
tech support agent says to a desperate customer, to /output/entry.txt
and prints it.
"""
import os

LINE = "I know your deadline's in ten minutes, so I restarted the server — the error's back, and now it sounds personally disappointed in you."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
