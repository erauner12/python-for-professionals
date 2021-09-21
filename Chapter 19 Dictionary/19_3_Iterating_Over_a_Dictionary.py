# If you use a dictionary as an iterator(e.g. in a for statement), it traverses the keys of the dictionary. For example:


d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])
# c 3
# b 2
# a 1

# The same is true when used in a comprehension
print([key for key in d])
# ['c', 'b', 'a']

# The items() method can be used to loop over both the key and value simultaneously:
for key, value in d.items():
    print(key, value)
# c 3
# b 2
# a 1

print(d.values())
for value in d.values():
    print(value)
# 3
# 2
# 1
