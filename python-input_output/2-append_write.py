#!/usr/bin/python3
"""Adding a string to a text file."""


def append_write(filename="", text=""):
    """Adding a string to a text file."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.append(text)
