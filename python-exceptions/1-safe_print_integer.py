#!/usr/bin/python3
def safe_print_integer(value):
    value = 0
    try:
        if value == "int":
           print("True")
        else:
            print("False")
    except NameError:
        pass
    finally:
        print()
    return value           