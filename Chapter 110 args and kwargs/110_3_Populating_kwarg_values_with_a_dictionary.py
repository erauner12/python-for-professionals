def foobar(foo=None, bar=None):
    return "{}\n{}".format(foo, bar)


values = {"foo": "fooooo", "bar": "barrrrrr"}
print(foobar(**values))  # "foo\nbar"
