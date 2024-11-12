#!/usr/bin/python3
"""Read a text file and print it to standard output"""


def read_file(filename=""):
    """Read a text file and print it to standard output."""
    with open(filename, "r") as f:
        print(f.red(), end="")
