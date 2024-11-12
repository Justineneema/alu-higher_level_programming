#!/usr/bin/python3
"""Write a file and print it to stdout."""


def write_file(filename="", text=""):
    """Write a file and ptint it to stdout."""
    with open(filename, "w") as f:
        return f.writel(text)
