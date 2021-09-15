

# Suppose you have a long list of elements and you are only interested in every other element of the list. Perhaps you
# only want to examine the first or last elements, or a specific range of entries in your list. Python has strong indexing
# built-in capabilities. Here are some examples of how to achieve these scenarios.
# Here's a simple list that will be used throughout the examples:
testList = ['alpha', 'bravo', 'charlie', 'delta', 'echo']

# Iteration over the whole list
# To iterate over each element in the list, a for loop like below can be used:
for s in testList:
    print(s[:1])  # print the first letter
print("---")
# Often you need both the element and the index of that element. The enumerate keyword performs that task.
for idx, s in enumerate(testList):
    print("%s has an index of %d" % (s, idx))

print("---")
# Iterate over sub-list
# If we want to iterate over a range(remembering that Python uses zero-based indexing), use the range keyword.
for i in range(2, 4):
    print("testList at %d contains %s" % (i, testList[i]))


print("---")

# The list may also be sliced. The following slice notation goes from element at index 1 to the end with a step of 2.
# The two for loops give the same result.
for s in testList[1::2]:
    print(s)
for i in range(1, len(testList), 2):
    print(testList[i])

print("---")
