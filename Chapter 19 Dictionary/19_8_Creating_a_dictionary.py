# Rules for creating a dictionary:

# Every key must be unique(otherwise it will be overridden)
# Every key must be hashable(can use the hash function to hash it
#                            otherwise TypeError will be thrown)
# There is no particular order for the keys.

# Creating and populating it with values
stock = {'eggs': 5, 'milk': 2}

# Or creating an empty dictionary
dictionary = {}

# And populating it after
dictionary['eggs'] = 5
dictionary['milk'] = 2

# Values can also be lists
mydict = {'a': [1, 2, 3], 'b': ['one', 'two', 'three']}

# Use list.append() method to add new elements to the values list
mydict['a'].append(4)  # => {'a': [1, 2, 3, 4], 'b': ['one', 'two', 'three']}
# => {'a': [1, 2, 3, 4], 'b': ['one', 'two', 'three', 'four']}

mydict['b'].append('four')
# We can also create a dictionary using a list of two-items tuples
iterable = [('eggs', 5), ('milk', 2)]


dictionary = dict(iterable)
print(dictionary)
# Or using keyword argument:

eggs = None
milk = None
dictionary = dict(eggs=5, milk=2)
print(dictionary)
