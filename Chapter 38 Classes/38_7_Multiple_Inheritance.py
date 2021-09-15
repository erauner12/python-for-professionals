

class Foo(object):
    foo = 'attr foo of Foo'  # this is what will be printed


class Bar(object):
    foo = 'attr foo of Bar'  # we won't see this.
    bar = 'attr bar of Bar'


class FooBar(Foo, Bar):
    foobar = 'attr foobar of FooBar'


# It can be simply stated that Python's MRO algorithm is
# 1. Depth first(e.g. FooBar then Foo) unless
# 2. a shared parent(object) is blocked by a child(Bar) and
# 3. no circular relationships allowed.

fb = FooBar()

print(fb.foo)
print(FooBar.mro())


print("---")


class Foo(object):
    def __init__(self):
        print("foo init")

    def foo_method(self):
        print("foo Method")


class Bar(object):
    def __init__(self):
        print("bar init")

    def bar_method(self):
        print("bar Method")


# class FooBar(Bar, Foo): # print bar init instead of foo init after foobar init
class FooBar(Foo, Bar):
    def __init__(self):
        print("foobar init")
        super(FooBar, self).__init__()

        # super(FooBar, self).foo_method()
        # super(FooBar, self).bar_method()


a = FooBar()

print(a)
# foobar init
# foo init

print(isinstance(a, FooBar))
print(isinstance(a, Foo))
print(isinstance(a, Bar))
# all True
