from collections import OrderedDict
d = OrderedDict()
d['first'] = 1
d['second'] = 2
d['third'] = 3
d['last'] = 4
# Outputs "first 1", "second 2", "third 3", "last 4"
for key in d:
    print(key, d[key])
