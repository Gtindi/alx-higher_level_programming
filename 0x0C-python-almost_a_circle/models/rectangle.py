#!/usr/bin/python3

"""This module contains `Rectangle` class."""


from models.base import Base


class Rectangle(Base):
    """The `Rectangle` class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Creates a `Rectangle`.

        Args:
            width(int): The `Rectangle` width
            height(int): The `Rectangle` height
            x(int): The `Rectangle` x
            y(int): The `Rectangle` y
            id(int): The `Rectangle` id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the `Rectangle` `width`."""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets `Rectangle` width.

        Args:
            value(int): The `width` of the `Rectangle`
        """

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns the `Rectangle` `height`."""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the `Rectangle` `height`.

        Args
            value(int): The `height` of the `Rectangle`
        """

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns the `Rectangle` `x`."""

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the `Rectangle` `x`.

        Args
            value(int): The `x` of the `Rectangle`
        """

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns the `Rectangle` `y`."""

        return self.__y

    @y.setter
    def y(self, value):
        """Sets the `Rectangle` `y`.

        Args
            value(int): The `y` of the `Rectangle`
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the `area` of the `Rectangle`"""

        return self.width * self.height

    def display(self):
        """Prints the `Rectangle` to stdout."""

        for i in range(self.y):
            print()
        for i in range(self.height):
            if i > 0:
                print("")
            for m in range(self.x):
                print(end=" ")
            for j in range(self.width):
                print("#", end="")
        print()

    def __str__(self):
        """Returns `Rectangle` as string."""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """Updates the `Rectangle`.

        Args:
            args(tuple): A variadic argument
        """

        if args is not None:
            attributes = ['id', 'width', 'height', 'x', 'y']

            for i, arg in enumerate(args):
                if i > len(attributes):
                    break
                setattr(self, attributes[i], arg)

        if (args is None or len(args) == 0) and kwargs is not None:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle."""

        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            "y": self.y
        }
