# __ magic method
# __init__ => constructor


class Point:
    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point2 = Point(3, 4)

print(point2.default_color)

# class level attributes are shared across all instances of the class
# since these objects point to the same class instance, it will appear
# that the changes are retroactive
Point.default_color = "yellow"

print(point2.default_color)

point = Point(1, 2)
point.draw()

print(point.x)
print(type(point))
print(isinstance(point, Point))

print(Point.default_color)
print(point.default_color)

# Factory method
point = Point.zero()
print(point)

# https://rszalski.github.io/magicmethods/
# magic methods inherited by classes allow us to construct certain default behaviors
# for example the __str__ magic method allows us to define __str__
# and customize its behavior, now print will call our new version of the __str__ method

print(point)
print(str(point))


# Comparison magic methods https://rszalski.github.io/magicmethods/#comparisons

# Some can be inferred.  If you build the GT operator, python will infer the less than operator
# implementation
pointOne = Point(1, 2)
pointTwo = Point(1, 2)
print(pointOne == pointTwo)

# Can add normal arithmetic operators too
# https://rszalski.github.io/magicmethods/#numeric
