#!/usr/bin/python3
"""Tasks 10 -
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square based off the Rectangle class
    """
    # Initializes based off Rectangle
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    # Print method
    def __str__(self):
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    # Update method for the object's attributes
    def update(self, *args, **kwargs):
        flag = 0
        if args is not None:
            flag = 1
        if len(args) > 0 and flag == 1:
            self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    # Returns a dictionary representation of the square's attributes
    def to_dictionary(self):
        atts = {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
        return atts

    # Getter & Setter
    @property
    def size(self):
        return super().width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
