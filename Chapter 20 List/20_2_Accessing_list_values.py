

# Python lists are zero-indexed, and act like arrays in other languages.
lst = [1, 2, 3, 4]


lst[0]  # 1
lst[1]  # 2
# Attempting to access an index outside the bounds of the list will raise an IndexError.
# lst[4]  # IndexError: list index out of range

# Negative indices are interpreted as counting from the end of the list.
lst[-1]  # 4
lst[-2]  # 3
# lst[-5]  # IndexError: list index out of range
# This is functionally equivalent to
lst[len(lst)-1]  # 4

# Lists allow to use slice notation as lst[start:end:step]. The output of the slice notation is a new list containing
# elements from index start to end-1. If options are omitted start defaults to beginning of list, end to end of list and
# step to 1:

lst[1:]  # [2, 3, 4]
lst[:3]  # [1, 2, 3]
lst[::2]  # [1, 3]
lst[::-1]  # [4, 3, 2, 1]
lst[-1:0:-1]  # [4, 3, 2]
lst[5:8]  # [] since starting index is greater than length of lst, returns empty list
lst[1:10]  # [2, 3, 4] same as omitting ending index

# With this in mind, you can print a reversed version of the list by calling
lst[::-1]  # [4, 3, 2, 1]

# When using step lengths of negative amounts, the starting index has to be greater than the ending index otherwise
# the result will be an empty list.
lst[3:1:-1]  # [4, 3]

# Using negative step indices are equivalent to the following code:
# reversed(lst)[0:2]  # 0 = 1 -1
# 2 = 3 - 1


# Advanced slicing
# When lists are sliced the __getitem__() method of the list object is called, with a slice object. Python has a builtin
# slice method to generate slice objects. We can use this to store a slice and reuse it later like so,
data = 'chandan purohit 22 2000'  # assuming data fields of fixed length
name_slice = slice(0, 15)
age_slice = slice(16, 18)
salary_slice = slice(19, None)
# now we can have more readable slices
print(data[name_slice])  # chandan purohit
print(data[age_slice])  # '22'
print(data[salary_slice])  # '2000'

# This can be of great use by providing slicing functionality to our objects by overriding __getitem__ in our class.
