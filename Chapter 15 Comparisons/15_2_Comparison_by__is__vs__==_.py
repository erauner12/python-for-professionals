

# A common pitfall is confusing the equality comparison operators is and == .
# a == b compares the value of a and b.
# a is b will compare the identities of a and b.
# To illustrate:
a = 'Python is fun!'
b = 'Python is fun!'
a == b  # returns True
a is b  # returns False
a = [1, 2, 3, 4, 5]
b = a  # b references a
a == b  # True
a is b  # True
b = a[:]  # b now references a copy of a
a == b  # True
a is b  # False [!!]

# Basically, is can be thought of as shorthand for id(a) == id(b).

# Beyond this, there are quirks of the run-time environment that further complicate things. Short strings and small
# integers will return True when compared with is, due to the Python machine attempting to use less memory for
# identical objects

a = 'short'
b = 'short'
c = 5
d = 5
a is b  # True
c is d  # True

# But longer strings and larger integers will be stored separately.
a = 'not so short'
b = 'not so short'
c = 1000
d = 1000
a is b  # False
c is d  # False

myvar = None
# You should use is to test for None:
if myvar is not None:
    # not None
    pass
if myvar is None:
    # None
    pass
