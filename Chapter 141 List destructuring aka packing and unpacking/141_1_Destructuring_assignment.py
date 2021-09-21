# Destructuring as values
a, b = (1, 2)
print(a)
# Prints: 1
print(b)
# Prints: 2
# If you try to unpack more than the length of the iterable, you'll get an error:

# a, b, c = [1]
# Raises: ValueError: not enough values to unpack (expected 3, got 1)


# Destructuring as a list
# You can unpack a list of unknown length using the following syntax:
head, *tail = [1, 2, 3, 4, 5]
# Here, we extract the first value as a scalar, and the other values as a list:
print(head)
# Prints: 1
print(tail)
# Prints: [2, 3, 4, 5]

# Which is equivalent to:
l = [1, 2, 3, 4, 5]
head = l[0]
tail = l[1:]

print("---")
# It also works with multiple elements or elements form the end of the list:
a, b, *other, z = [1, 2, 3, 4, 5]
print(a, b, z, other)
# Prints: 1 2 5 [3, 4]

print("---")
# Ignoring values in destructuring assignments
# If you're only interested in a given value, you can use _ to indicate you aren’t interested. Note: this will still set _, just
# most people don’t use it as a variable.
a, _ = [1, 2]
print(a)
# Prints: 1
a, _, c = (1, 2, 3)
print(a)
# Prints: 1

print(c)
# Prints: 3

print("---")
# Ignoring lists in destructuring assignments
# Finally, you can ignore many values using the * _ syntax in the assignment:
a, *_ = [1, 2, 3, 4, 5]
print(a)
# Prints: 1

# which is not really interesting, as you could using indexing on the list instead. Where it gets nice is to keep first and
# last values in one assignment:
a, *_, b = [1, 2, 3, 4, 5]
print(a, b)
# Prints: 1 5

print("---")


# or extract several values at once:
a, _, b, _, c, *_ = [1, 2, 3, 4, 5, 6]
print(a, b, c)
# Prints: 1 3 5
