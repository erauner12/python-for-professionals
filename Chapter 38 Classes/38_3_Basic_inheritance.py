
class BaseClass(object):
    pass


class DerivedClass(BaseClass):
    pass


class Rectangle():
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return 2 * (self.w + self.h)


class Square(Rectangle):
    def __init__(self, s):
        # call parent constructor, w and h are both s
        super(Square, self).__init__(s, s)
        self.s = s


# subclass check
print(issubclass(Square, Rectangle))
# Output: True

r = Rectangle(3, 4)

print(r.area())
print(isinstance(r, Rectangle))
print(isinstance(r, Square))
# Output: False
# A rectangle is not a square

# Output: 12
print(r.perimeter())

# Output: 14

s = Square(2)
print(isinstance(s, Rectangle))
# Output: True
# A square is a rectangle
print(isinstance(s, Square))
# Output: True

print(s.area())
# Output: 4
print(s.perimeter())
# Output: 8
