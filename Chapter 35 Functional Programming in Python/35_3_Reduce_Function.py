
from functools import reduce


# Reduce takes a function and a collection of items. It returns a value that is created by combining the items.
# This is a simple reduce. It returns the sum of all the items in the collection.

total = reduce(lambda a, x: a + x, [0, 1, 2, 3, 4])

print(total)
