
import copy
import datetime
from operator import itemgetter, attrgetter
import pprint
pp = pprint.PrettyPrinter(indent=4)

a = [1, 2, 3, 4, 5]

# append(value) – appends a new element to the end of the list.
# Append values 6, 7, and 7 to the list
a.append(6)
a.append(7)
a.append(7)
# a: [1, 2, 3, 4, 5, 6, 7, 7]
# Append another list
b = [8, 9]
a.append(b)
# a: [1, 2, 3, 4, 5, 6, 7, 7, [8, 9]]


# Append an element of a different type, as list elements do not need to have the same type
my_string = "hello world"
a.append(my_string)
# a: [1, 2, 3, 4, 5, 6, 7, 7, [8, 9], "hello world"]


# Note that the append() method only appends one new element to the end of the list. If you append a list to
# another list, the list that you append becomes a single element at the end of the first list.
# Appending a list to another list
a = [1, 2, 3, 4, 5, 6, 7, 7]
b = [8, 9]
a.append(b)
# a: [1, 2, 3, 4, 5, 6, 7, 7, [8, 9]]
a[8]
# Returns: [8,9]


# extend(enumerable) – extends the list by appending elements from another enumerable.

a = [1, 2, 3, 4, 5, 6, 7, 7]
b = [8, 9, 10]
# Extend list by appending all elements from b
a.extend(b)
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
# Extend list with elements from a non-list enumerable:
a.extend(range(3))
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10, 0, 1, 2]


# Lists can also be concatenated with the + operator. Note that this does not modify any of the original lists:
a = [1, 2, 3, 4, 5, 6] + [7, 7] + b
# a: [1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]


# index(value, [startIndex]) – gets the index of the first occurrence of the input value. If the input value is
# not in the list a ValueError exception is raised. If a second argument is provided, the search is started at that
# specified index.

# gets the item number in array that it is
a.index(7)
# Returns: 6
# a.index(49)  # ValueError, because 49 is not in a.
a.index(7, 7)
# Returns: 7

# a.index(7, 8)  # ValueError, because there is no 7 starting at index 8


# insert(index, value) – inserts value just before the specified index. Thus after the insertion the new
# element occupies position index.
a.insert(0, 0)  # insert 0 at position 0
a.insert(2, 5)  # insert 5 at position 2
# a: [0, 1, 5, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]


# pop([index]) – removes and returns the item at index. With no argument it removes and returns the last
# element of the list.

a.pop(2)
# Returns: 5
# a: [0, 1, 2, 3, 4, 5, 6, 7, 7, 8, 9, 10]
a.pop(8)
# Returns: 7
# a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# With no argument:
a.pop()
# Returns: 10
# a: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# remove(value) – removes the first occurrence of the specified value. If the provided value cannot be found, a
# ValueError is raised.
a.remove(0)
a.remove(9)
# a: [1, 2, 3, 4, 5, 6, 7, 8]
# a.remove(10)
# ValueError, because 10 is not in a


# reverse() – reverses the list in -place and returns None.
a.reverse()
# a: [8, 7, 6, 5, 4, 3, 2, 1]
# There are also other ways of reversing a list.


# count(value) – counts the number of occurrences of some value in the list.
a.count(7)
# Returns: 2

# sort() – sorts the list in numerical and lexicographical order and returns None.
a.sort()
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# Sorts the list in numerical order

# Lists can also be reversed when sorted using the reverse = True flag in the sort() method.
a.sort(reverse=True)
# a = [8, 7, 6, 5, 4, 3, 2, 1]


# If you want to sort by attributes of items, you can use the key keyword argument:


class Person(object):
    def __init__(self, name, birthday, height):
        self.name = name
        self.birthday = birthday
        self.height = height

    def __repr__(self):
        return self.name


l = [Person("John Cena", datetime.date(1992, 9, 12), 175),
     Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
     Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]

l.sort(key=lambda item: item.name)
# l: [Chuck Norris, John Cena, Jon Skeet]
l.sort(key=lambda item: item.birthday)
# l: [Chuck Norris, Jon Skeet, John Cena]
l.sort(key=lambda item: item.height)
# l: [John Cena, Chuck Norris, Jon Skeet]

# In case of list of dicts the concept is the same:
l = [{'name': 'John Cena', 'birthday': datetime.date(1992, 9, 12), 'height': 175},
     {'name': 'Chuck Norris', 'birthday': datetime.date(
         1990, 8, 28), 'height': 180},
     {'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6), 'height': 185}]

l.sort(key=lambda item: item['name'])
# l: [Chuck Norris, John Cena, Jon Skeet]
l.sort(key=lambda item: item['birthday'])
# l: [Chuck Norris, Jon Skeet, John Cena]
l.sort(key=lambda item: item['height'])
# l: [John Cena, Chuck Norris, Jon Skeet]


# Sort by sub dict:
l = [{'name': 'John Cena', 'birthday': datetime.date(1992, 9, 12), 'size': {'height': 175,
                                                                            'weight': 100}},
     {'name': 'Chuck Norris', 'birthday': datetime.date(1990, 8, 28), 'size': {'height': 180,
                                                                               'weight': 90}},
     {'name': 'Jon Skeet', 'birthday': datetime.date(1991, 7, 6), 'size': {'height': 185,
                                                                           'weight': 110}}]
l.sort(key=lambda item: item['size']['height'])
# l: [John Cena, Chuck Norris, Jon Skeet]


# Better way to sort using attrgetter and itemgetter

# Lists can also be sorted using attrgetter and itemgetter functions from the operator module. These can help
# improve readability and reusability. Here are some examples,
people = [{'name': 'chandan', 'age': 20, 'salary': 2000},
          {'name': 'chetan', 'age': 18, 'salary': 5000},
          {'name': 'guru', 'age': 30, 'salary': 3000}]
by_age = itemgetter('age')
by_salary = itemgetter('salary')
people.sort(key=by_age)  # in-place sorting by age
# people.sort(key=by_salary)  # in-place sorting by salary

pp.pprint(people)


# itemgetter can also be given an index. This is helpful if you want to sort based on indices of a tuple.
list_of_tuples = [(1, 2), (3, 4), (5, 0)]
list_of_tuples.sort(key=itemgetter(1))

print(list_of_tuples)  # [(5, 0), (1, 2), (3, 4)]

# Use the attrgetter if you want to sort by attributes of an object,
persons = [Person("John Cena", datetime.date(1992, 9, 12), 175),
           Person("Chuck Norris", datetime.date(1990, 8, 28), 180),
           Person("Jon Skeet", datetime.date(1991, 7, 6), 185)]  # reusing Person class from above
# example
persons.sort(key=attrgetter('name'))  # sort by name
by_birthday = attrgetter('birthday')
persons.sort(key=by_birthday)  # sort by birthday
pp.pprint(persons)


# clear() – removes all items from the list

# Replication – multiplying an existing list by an integer will produce a larger list consisting of that many copies
# of the original. This can be useful for example for list initialization:
b = ["blah"] * 3
# b = ["blah", "blah", "blah"]
b = [1, 3, 5] * 5
# [1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5, 1, 3, 5]


# Copying

# The default assignment "=" assigns a reference of the original list to the new name. That is, the original name
# and new name are both pointing to the same list object. Changes made through any of them will be reflected
# in another. This is often not what you intended.
b = a
a.append(6)
# b: [1, 2, 3, 4, 5, 6]


old_list = [1, 2, 3]
# If you want to create a copy of the list you have below options.
# You can slice it:
new_list = old_list[:]
# You can use the built in list() function:
new_list = list(old_list)
# You can use generic copy.copy():
# inserts references to the objects found in the original.
new_list = copy.copy(old_list)
# This is a little slower than list() because it has to find out the datatype of old_list first.
# If the list contains objects and you want to copy them as well, use generic copy.deepcopy():
# inserts copies of the objects found in the original.
new_list = copy.deepcopy(old_list)
# Obviously the slowest and most memory-needing method, but sometimes unavoidable.
