from itertools import chain
from collections import ChainMap

fish = {'name': "Nemo",
        'hands': "fins",
        'special': "gills"}

dog = {'name': "Clifford",
       'hands': "paws",
       'color': "red"}

fishdog = {**fish, **dog}
print(fishdog)
# As this example demonstrates, duplicate keys map to their lattermost value(for example "Clifford" overrides "Nemo").
# {'name': 'Clifford',
# 'hands': 'paws',
# 'special': 'gills',
# 'color': 'red'}

print("---")
# With this technique the foremost value takes precedence for a given key rather than the last ("Clifford" is thrown out in favor of "Nemo")
print(dict(ChainMap(fish, dog)))

# This uses the lattermost value, as with the ** -based technique for merging("Clifford" overrides "Nemo").
print(dict(chain(fish.items(), dog.items())))

# This uses the lattermost value, as with the **-based technique for merging ("Clifford" overrides "Nemo").
fish.update(dog)
print(fish)
# dict.update uses the latter dict to overwrite the previous one.
