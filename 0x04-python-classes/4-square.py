#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Square class with size checks

        Args:
            size (int): size of square. Defaults to 0.

        Raises:
            ValueError: size must be greater than 0
            TypeError: size must be an integer
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
    
    def area(self):
        """Returns the area of the square

        Returns:
            int: size squared
        """
        return self.__size**2

    def my_print(self):
        """Prints out a # square
        """
        if self.__size is 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                    if j is self.__size - 1:
                        print("")



    @property
    def size(self):
        """Returns the value of size

        Returns:
            int: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of size

        Args:
            value (int): size

        Raises:
            ValueError: size must be greater than 0
            TypeError: size must be an integer
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")
