

# One common pitfall when using dictionaries is to access a non-existent key. This typically results in a KeyError
# exception
mydict = {"there": "testing"}
# print(mydict['not there'])
# Traceback(most recent call last):
#     File "<stdin>", line 1, in <module >
# KeyError: 'not there'


# Which returns mydict[key] if it exists, but otherwise returns default_value. Note that this doesn't add key to
# mydict. So if you want to retain that key value pair, you should use mydict.setdefault(key, default_value),
# which does store the key value pair.

key = "there"
default_value = "default because it is not there"
value = mydict.get(key, default_value)

print(value)
nonexistentKey = "jfskldfj"
value = mydict.get(nonexistentKey, default_value)
print(value)


print("---")
mydict = {}
print(mydict)
# {}
print(mydict.get("foo", "bar"))
# bar
print(mydict)
# {}
print(mydict.setdefault("foo", "bar"))
# bar
print(mydict)
# {'foo': 'bar'}


# An alternative way to deal with the problem is catching the exception
try:
    value = mydict[key]
except KeyError:
    value = default_value


# You could also check if the key is in the dictionary
if key in mydict:
    value = mydict[key]
else:
    value = default_value
