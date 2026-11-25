# makefun-turning-it-off
Entry for make.fun Have You Tried Turning It Off?: a program that writes one original funny tech-support line to /output/entry.txt

## What it does
The program builds a single original line that a hopeless tech support
agent says to a desperate customer, validates that the line is one line
long and under 200 characters, then writes it to /output/entry.txt and
prints it to stdout.

## How to run
Run the entrypoint with Python 3:

    python3 main.py

The script creates /output if it does not exist yet, so it works from a
fresh checkout with no setup beyond a Python 3 interpreter.

## Output
The entry file /output/entry.txt contains exactly one line, 134
characters long, ending with a newline. The same line is printed to
stdout for a quick visual check.
