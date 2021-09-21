# When working with dictionaries, it's often necessary to access all the keys and values in the dictionary, either in a
# for loop, a list comprehension, or just as a plain list.
# Given a dictionary like:

mydict = {
    'a': '1',
    'b': '2'
}


print(mydict.keys())
# Python2: ['a', 'b']
# Python3: dict_keys(['b', 'a'])


# If instead you want a list of values, use the values() method:
print(mydict.values())
# Python2: ['1', '2']
# Python3: dict_values(['2', '1'])


# If you want to work with both the key and its corresponding value, you can use the items() method:
print(mydict.items())
# Python2: [('a', '1'), ('b', '2')]
# Python3: dict_items([('b', '2'), ('a', '1')])
