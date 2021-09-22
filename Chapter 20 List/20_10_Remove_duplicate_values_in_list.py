import collections
# Removing duplicate values in a list can be done by converting the list to a set(that is an unordered collection of
# distinct objects). If a list data structure is needed, then the set can be converted back to a list using the function
# list():

names = ["aixk", "duke", "edik", "tofp", "duke"]
list(set(names))
# Out: ['duke', 'tofp', 'aixk', 'edik']
# Note that by converting a list to a set the original ordering is lost.

# To preserve the order of the list one can use an OrderedDict
collections.OrderedDict.fromkeys(names).keys()
# Out: ['aixk', 'duke', 'edik', 'tofp']
