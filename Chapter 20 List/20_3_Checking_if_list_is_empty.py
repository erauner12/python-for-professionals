

# The emptiness of a list is associated to the boolean False, so you don't have to check len(lst) == 0, but just lst
# or not lst
lst = []
if not lst:
    print("list is empty")
# Output: list is empty
