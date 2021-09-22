

# Use len() to get the one-dimensional length of a list.
len(['one', 'two'])  # returns 2
len(['one', [2, 3], 'four'])  # returns 3, not 4
# len() also works on strings, dictionaries, and other data structures similar to lists.

# Note that len() is a built-in function, not a method of a list object.
# Also note that the cost of len() is O(1), meaning it will take the same amount of time to get the length of a list
# regardless of its length.
