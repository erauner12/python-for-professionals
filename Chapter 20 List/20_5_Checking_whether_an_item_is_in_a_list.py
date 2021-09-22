

# Python makes it very simple to check whether an item is in a list. Simply use the in operator.
lst = ['test', 'twest', 'tweast', 'treast']
'test' in lst
# Out: True
'toast' in lst
# Out: False


# Note: the in operator on sets is asymptotically faster than on lists. If you need to use it many times on
# potentially large lists, you may want to convert your list to a set, and test the presence of elements on
# the set.
slst = set(lst)
'test' in slst
# Out: True
