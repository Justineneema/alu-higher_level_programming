#!/usr/bin/python3
"""
Module that defines a rectangle
 """


class Rectangle:
    """
    class to define a rectangle
    """
    def __init__(self, width=0, height=0):

     def width(self, value, width=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

     def height(self, value, height=0):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height    
        


    