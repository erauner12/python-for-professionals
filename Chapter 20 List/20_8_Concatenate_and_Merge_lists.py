

# The simplest way to concatenate list1 and list2:
# merged = list1 + list2


# zip returns a list of tuples, where the i-th tuple contains the i-th element from each of the argument
# sequences or iterables:
import itertools
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist):
    print(a, b)
# Output:
# a1 b1
# a2 b2
# a3 b3

print("---")
# If the lists have different lengths then the result will include only as many elements as the shortest one:
alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3', 'b4']
for a, b in zip(alist, blist):
    print(a, b)
# Output:
# a1 b1
# a2 b2
# a3 b3
alist = []
len(list(zip(alist, blist)))
# Output:
# 0

print("---")
# For padding lists of unequal length to the longest one with Nones use itertools.zip_longest
# (itertools.izip_longest in Python 2)
alist = ['a1', 'a2', 'a3']
blist = ['b1']
clist = ['c1', 'c2', 'c3', 'c4']
for a, b, c in itertools.zip_longest(alist, blist, clist):
    print(a, b, c)
# Output:
# a1 b1 c1
# a2 None c2
# a3 None c3
# None None c4


# Insert to a specific index values:
alist = [123, 'xyz', 'zara', 'abc']
alist.insert(3, [2009])
print("Final List :", alist)
# Output:
# Final List: [123, 'xyz', 'zara', 2009, 'abc']
