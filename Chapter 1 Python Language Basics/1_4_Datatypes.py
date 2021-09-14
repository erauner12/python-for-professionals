
# bool: A boolean value of either True or False. Logical operations like and, or, not can be performed on booleans
x = 1
y = 1  # if you put 0, will be false

print("next")
if x or y:
    print(x)
    print(y)  # if x is False then y otherwise x


# y = 0 # this will break the next condition
print("next")
if x and y:
    print(x)
    print(y)  # if x is False then x otherwise y


y = 0  # this will resolve as true and print y since it is false
print("next")
if not y:
    print(y)  # if x is True then False, otherwise True


# In Python 2.x and in Python 3.x, a boolean is also an int. The bool type is a subclass of the int type and True and
# False are its only instances:
issubclass(bool, int)  # True
isinstance(True, bool)  # True
isinstance(False, bool)  # True


# If boolean values are used in arithmetic operations, their integer values (1 and 0 for True and False) will be used to
# return an integer result:
True + False == 1  # 1 + 0 == 1
True * True == 1  # 1 * 1 == 1


# Integers in Python are of arbitrary sizes.
# Note: in older versions of Python, a long type was available and this was distinct from int. The two have
# been unified
a = 2
b = 100
c = 123456789
d = 38563846326424324

# float: Floating point number; precision depends on the implementation and system architecture, for
# CPython the float datatype corresponds to a C double.
a = 2.0
b = 100.e0
c = 123456789.e1

# complex: Complex numbers
a = 2 + 1j
b = 100 + 10j

# reversed: A reversed order of str with reversed function
a = reversed('hello')
print(a)


# tuples (cannot change)
a = (1, 2, 3)
b = ('a', 1, 'python', (1, 2))
# b[2] = 'something else' # returns a TypeError

# list: An ordered collection of n values (n >= 0)
a = [1, 2, 3]
b = ['a', 1, 'python', (1, 2), [1, 2]]
b[2] = 'something else'  # allowed
print(b[2])


# set: An unordered collection of unique values. Items must be hashable.
a = {1, 2, 'a'}


# dict: An unordered collection of unique key-value pairs; keys must be hashable.
a = {1: 'one',
     2: 'two'}
b = {'a': [1, 2, 3],
     'b': 'a string'}
print(b)

# An object is hashable if it has a hash value which never changes during its lifetime (it needs a __hash__()
# method), and can be compared to other objects (it needs an __eq__() method). Hashable objects which
# compare equality must have the same hash value


# None type

a = None  # No value will be assigned. Any valid datatype can be assigned later
print(a)


# In python, we can check the datatype of an object using the built-in function type.
a = '123'
print(type(a))

# Out: <class 'str'>
b = 123
print(type(b))
# Out: <class 'int'>


# In conditional statements it is possible to test the datatype with isinstance. However, it is usually not encouraged
# to rely on the type of the variable.
i = "6"
# i = 6
if isinstance(i, int):
    i += 1
elif isinstance(i, str):
    i = int(i)
    i += 1
print(i)
# Out: 7


# To test if something is of NoneType:
x = None
if x is None:
    print('Not a surprise, I just defined x as None.')


# Converting between datatypes
# You can perform explicit datatype conversion.
# For example, '123' is of str type and it can be converted to integer using int function.
a = '123'
b = int(a)

# Converting from a float string such as '123.456' can be done using float function.

a = '123.456'
b = float(a)
# c = int(a)  # ValueError: invalid literal for int() with base 10: '123.456'
# d = int(b)  # 123
print(a)


# You can also convert sequence or collection types
a = 'hello'
a = list(a)  # ['h', 'e', 'l', 'l', 'o']
set(a)  # {'o', 'e', 'l', 'h'}
tuple(a)  # ('h', 'e', 'l', 'l', 'o')
print(type(a))


# newlines
normal = 'foo\nbar'  # foo newline bar
print(normal)

escaped = 'foo\\nbar'  # foo\nbar
print(escaped)

raw = r'foo\nbar'  # foo\nbar
print(raw)


# Mutable and Immutable Data Types
# An object is called mutable if it can be changed. For example, when you pass a list to some function, the list can be
# changed:
def fappend(m):
    m.append(3)  # adds a number to the list. This is a mutation.


x = [1, 2]
print(x)
fappend(x)
print(x)

if x == [1, 2]:
    print(x)  # False now, since an item was added to the list

# An object is called immutable if it cannot be changed in any way. For example, integers are immutable, since there's
# no way to change them:


def bar():
    x = (1, 2)
    g(x)  # does not exist
    x == (1, 2)  # Will always be True, since no function can change the object (1, 2)
