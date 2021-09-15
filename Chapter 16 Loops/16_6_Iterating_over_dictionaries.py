

# Considering the following dictionary:
d = {"a": 1, "b": 2, "c": 3}
# To iterate through its keys, you can use:
for key in d:
    print(key)

print("---")
# same as
for key in d.keys():
    print(key)

print("---")
# To iterate through its values, use:
for value in d.values():
    print(value)

print("---")
# To iterate through its keys and values, use:
for key, value in d.items():
    print(key, "::", value)
