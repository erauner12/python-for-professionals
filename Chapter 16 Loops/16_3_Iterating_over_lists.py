

# To iterate through a list you can use for:
for x in ['one', 'two', 'three', 'four']:
    print(x)


# The range function generates numbers which are also often used in a for loop
for x in range(1, 6):
    print(x)


# If you want to loop though both the elements of a list and have an index for the elements as well, you can use
# Python's enumerate function:
for index, item in enumerate(['one', 'two', 'three', 'four']):
    print(index, '::', item)


xList = map(lambda e: e.upper(), ['one', 'two', 'three', 'four'])

# NB: in Python 3.x map returns an iterator instead of a list so you in case you need a list you have to cast the result
# print(list(x))
print(xList)
print(list(xList))
for x in xList:
    print(x)
