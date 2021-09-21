# Filter takes a function and a collection. It returns a collection of every item for which the function returned True.
arr = [1, 2, 3, 4, 5, 6]
print([i for i in filter(lambda x:x > 4, arr)])  # outputs[5,6]
