#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        inside = a / b
    except Exception as e:
        inside = None
    finally:
        print("Inside result: {}".format(inside))
    return inside
