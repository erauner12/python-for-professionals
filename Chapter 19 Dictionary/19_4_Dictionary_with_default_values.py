from collections import defaultdict

d = defaultdict(int)
d['key']  # 0
d['key'] = 5
print(d['key'])  # 5

d = defaultdict(lambda: 'empty')
d['key']  # 'empty'
d['key'] = 'full'
print(d['key'])  # 'full'


# [*] Alternatively, if you must use the built-in dict class, using dict.setdefault() will allow you to create a default
# whenever you access a key that did not exist before:
d = {}

d.setdefault('Another_key', []).append("This worked!")
print(d)
# {'Another_key': ['This worked!']}
