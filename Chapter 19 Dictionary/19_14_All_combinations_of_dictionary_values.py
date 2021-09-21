import pprint


# Given a dictionary such as the one shown above, where there is a list representing a set of values to explore for the
# corresponding key. Suppose you want to explore "x" = "a" with "y" = 10, then "x" = "a" with"y" = 10, and so on until
# you have explored all possible combinations.
# You can create a list that returns all such combinations of values using the following code.

import itertools
options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]
}

pp = pprint.PrettyPrinter(indent=4)

options = {
    "x": ["a", "b"],
    "y": [10, 20, 30]}
keys = options.keys()
values = (options[key] for key in keys)
combinations = [dict(zip(keys, combination))
                for combination in itertools.product(*values)]


pp.pprint(combinations)
