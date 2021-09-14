
import datetime
s = """w'o'w"""
print(repr(s))
print(str(s))
# repr shows everything in the string whereas str shows human readable string

today = datetime.datetime.now()
print(repr(today))
print(str(today))
# another example

# When writing a class, you can override these methods to do whatever you want:
# Using the below class we can see the results:


class Represent(object):
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return "Represent(x={},y=\"{}\")".format(self.x, self.y)

    def __str__(self):
        return "Representing x as {} and y as {}".format(self.x, self.y)


r = Represent(1, "Hopper")
print(r)  # prints __str__
print(r.__repr__)  # prints __repr__: '<bound method Represent.__repr__ of
Represent(x=1, y="Hopper")
rep = r.__repr__()  # sets the execution of __repr__ to a new variable
print(rep)  # prints 'Represent(x=1,y="Hopper")'
r2 = eval(rep)  # evaluates rep
print(r2)  # prints __str__ from new object
print(r2 == r)  # prints 'False' because they are different objects
