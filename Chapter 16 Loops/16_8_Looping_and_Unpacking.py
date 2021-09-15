
collection = [('a', 'b', 'c'), ('x', 'y', 'z'), ('1', '2', '3')]
# instead of doing something like this:
for item in collection:
    i1 = item[0]
    i2 = item[1]
    i3 = item[2]
    print(i1, i2, i3)
    print(item)
    # logic

print("---")
# or something like this
for item in collection:
    i1, i2, i3 = item
    print(item)
    # logic

print("---")
# You can simply do this:
for i1, i2, i3 in collection:
    print(i1, i2, i3)
