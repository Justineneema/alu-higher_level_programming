#!/usr/bin/python3
def safe_print_integer(my_list=[], x=0):
    count = 0
    try:
        print("{:d}".format(x))
        count +=1
        return True
    except Exception:
        return False
    finally:
        print()
    return count      