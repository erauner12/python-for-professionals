

# For immutable elements(e.g. None, string literals etc.):
my_list = [None] * 10
my_list = ['test'] * 10


# For mutable elements, the same construct will result in all elements of the list referring to the same object, for
# example, for a set:
my_list = [{1}] * 10
print(my_list)
# [{1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}, {1}]
my_list[0].add(2)
print(my_list)
# [{1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}, {1, 2}]


# Instead, to initialize the list with a fixed number of different mutable objects, use:
my_list = [{1} for _ in range(10)]
