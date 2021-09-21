

# mapping in python

d = {}  # empty dict
d = {'key': 'value'}  # dict with initial values

print(d)

otherdict = {"key2": "value2", "key3": "value3"}

# Also unpacking one or multiple dictionaries with the literal syntax is possible
# makes a shallow copy of otherdict
d = {**otherdict}
print(d)

yetanotherdict = {"key4": "value4", "key5": "value5"}
# also updates the shallow copy with the contents of the yetanotherdict.
# merge two dicts
d = {**otherdict, **yetanotherdict}
print(d)

# populating with list comprehension (list of lists)
d = {k: v for k, v in [['key', 'value'], ['key2', 'val2']]}
print(d)


# modifying a dict
# To add items to a dictionary, simply create a new key with a value:
d['newkey'] = 42
print(d)

d['new_list'] = [1, 2, 3]
d['new_dict'] = {'nested_dict': 1}
print(d)
del d['newkey']
print(d)
