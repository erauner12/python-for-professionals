# Map takes a function and a collection of items. It makes a new, empty collection, runs the function on each item in
# the original collection and inserts each return value into the new collection. It returns the new collection.
# This is a simple map that takes a list of names and returns a list of the lengths of those names:

name_lengths = map(len, ["Mary", "Isla", "Sam"])

print(name_lengths)
for i in name_lengths:
    print(i)
