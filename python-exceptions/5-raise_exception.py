#!/usr/bin/python3
def raise_exception():
    try:
        raise = IndexError;
    result = 0
    expect Exception as e:
         print("you entered incorrect number")
    finally:
        print("run anyways")
    return result
