#!/usr/bin/python3
"""
rectanle module
"""
from models.base import Base


class Rectangle(Base):
    """
    rectangle base child
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init - initialization
        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: x position
            y: y position
            id: object id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        self.check('width', width)
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        self.check('width', height)
        self.__height = height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        x setter
        """
        self.check('x', x, False)
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        self.check('y', y, False)
        self.__y = y

    def check(self, key, value, less_eq=True):
        """
        check the vlaues and attributes
        """
        if not isinstance(value, int):
            raise TypeError(f"{key} must be an integer")
        if less_eq:
            if value <= 0:
                raise ValueError(f"{key} must be > 0")
        else:
            if value < 0:
                raise ValueError(f"{key} must be > 0")

    def area(self):
        """
        calculates area of rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints rectangle
        """
        for y in range(self.y):
            print()
        for column in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for row in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """
        custom str
        """
        return (
            f"[Rectangle] ({id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """
        list = (self.id, self.width, self.height, self.x, self.y)
        if args:
            self.id, self.width, self.height, self.x, self.y = \
                    args + list[len(args):len(list)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle.
        """
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
