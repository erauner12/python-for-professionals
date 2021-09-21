def foobar(foo=None, bar=None):
    return "{}\n{}".format(foo, bar)


values = {"foo": "foo", "bar": "bar"}
print(foobar(**values))  # "foobar"
