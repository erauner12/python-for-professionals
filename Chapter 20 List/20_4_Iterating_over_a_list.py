

# Python supports using a for loop directly on a list:
my_list = ['foo', 'bar', 'baz']
for item in my_list:
    print(item)
# Output: foo
# Output: bar
# Output: baz


# You can also get the position of each item at the same time:
for (index, item) in enumerate(my_list):
    print('The item in position {} is: {}'.format(index, item))
# Output: The item in position 0 is: foo
# Output: The item in position 1 is: bar
# Output: The item in position 2 is: baz


# The other way of iterating a list based on the index value:
for i in range(0, len(my_list)):
    print(my_list[i])
# output:
# foo
# bar
# baz

print("---")
# Note that changing items in a list while iterating on it may have unexpected results:
for item in my_list:
    if item == 'foo':
        del my_list[0]
    print(item)
# Output: foo
# Output: baz
