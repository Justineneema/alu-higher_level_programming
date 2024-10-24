#!/usr/bin/python3


def uppercase(str):
    result = ""
    for char in str:
        # Check if character is lowercase (ASCII values 97-122)
        if ord('a') <= ord(char) <= ord('z'):
            # Convert to uppercase by subtracting 32 from ASCII value
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
