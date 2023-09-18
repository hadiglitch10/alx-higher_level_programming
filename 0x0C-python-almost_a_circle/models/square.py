#!/usr/bin/python3
"""
square module
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init - initializer
        Args:
            size: of square
            x: x pos
            y: y pos
            id: its id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        size getter
        """
        return self.width
    
    @size.setter
    def size(self, size):
        """ size setter"""
        self.width = size
        self.height = size

    def __str__(self):
        """
        overriden __str__ method
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width) 

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        list = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                    args + list[len(args):len(list)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)
    
    def to_dictionary(self):
        """
        dic representation
        """
        return {'id':self.id, 'x':self.x, 'size':self.size, 'y':self.y}
