import helloWorld
import math
print(pow(2, 3))  # to the power of


# To check the built in function in python we can use dir(). If called without an argument, return the names in the
# current scope. Else, return an alphabetized list of names comprising(some of) the attribute of the given object, and
# of attributes reachable from it.
print(dir(__builtins__))

print(help(max))

print(dir(math))
print(math.__doc__)
print(math.sqrt(16))  # 4.0


print(helloWorld.__doc__)
# 'This is the module docstring.'
print(helloWorld.sayHello.__doc__)
# 'This is the function docstring.'


# For any user defined type, its attributes, its class's attributes, and recursively the attributes of its class's base
# classes can be retrieved using dir()

class MyClassObject(object):
    pass


print(dir(MyClassObject))
