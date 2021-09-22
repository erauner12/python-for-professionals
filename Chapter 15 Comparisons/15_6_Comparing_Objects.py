
# In order to compare the equality of custom classes, you can override == and != by defining __eq__ and __ne__
# methods. You can also override __lt__ ( < ), __le__ ( <= ), __gt__ ( > ), and __ge__ ( > ). Note that you only need to
# override two comparison methods, and Python can handle the rest ( == is the same as not < and not > , etc.)

class Foo(object):
    def __init__(self, item):
        self.my_item = item

    def __eq__(self, other):
        return self.my_item == other.my_item


a = Foo(5)
b = Foo(5)
a == b  # True
a != b  # False
a is b  # False


# Note that this simple comparison assumes that other(the object being compared to) is the same object type.
# Comparing to another type will throw an error:


class Bar(object):
    def __init__(self, item):
        self.other_item = item

    def __eq__(self, other):
        return self.other_item == other.other_item

    def __ne__(self, other):
        return self.other_item != other.other_item


c = Bar(5)
# a == c  # throws AttributeError: 'Foo' object has no attribute 'other_item'

# Checking isinstance() or similar will help prevent this(if desired).
