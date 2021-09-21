
# The dir() function can be used to get a list of the members of a class:
print(dir(list))

# It is common to look only for "non-magic" members. This can be done using a simple comprehension that lists
# members with names not starting with __:

print([m for m in dir(list) if not m.startswith('__')])

# A singleton is a pattern that restricts the instantiation of a class to one instance/object. For more info on python
# singleton design patterns


class Singleton:
    def __new__(cls):
        try:
            it = cls.__it__
        except AttributeError:
            it = cls.__it__ = object.__new__(cls)
        return it

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__.upper())

    def __eq__(self, other):
        return other is self


# Another method is to decorate your class. Following the example from this answer create a Singleton class:

class Singleton:
    """
    A non-thread-safe helper class to ease implementing singletons.
    This should be used as a decorator -- not a metaclass -- to the
    class that should be a singleton.
    The decorated class can define one `__init__` function that
    takes only the `self` argument. Other than that, there are
    no restrictions that apply to the decorated class.
    To get the singleton instance, use the `Instance` method. Trying
    to use `__call__` will result in a `TypeError` being raised.
    Limitations: The decorated class cannot be inherited from.
    """

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.
        """
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)


# To use you can use the Instance method

@Singleton
class Single:
    def __init__(self):
        self.name = None
        self.val = 0

    def getName(self):
        print(self.name)


x = Single.Instance()
y = Single.Instance()
x.name = 'I\'m single'
x.getName()  # outputs I'm single
y.getName()  # outputs I'm single
