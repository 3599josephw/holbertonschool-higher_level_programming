#!/usr/bin/python3
"""Tasks 10 -
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Creates a Square based off the Rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes based off Rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print method"""
        return "[Square] ({}) {}/{} - {}".\
            format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update method for the object's attributes"""
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

    def to_dictionary(self):
        """Returns a dictionary representation of the square's attributes"""
        atts = {'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y}
        return atts

    @property
    def size(self):
        """Getter"""
        return super().width

    @size.setter
    def size(self, value):
        """Setter"""
        self.width = value
        self.height = value
