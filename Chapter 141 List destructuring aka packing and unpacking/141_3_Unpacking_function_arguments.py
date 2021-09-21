# When you want to create a function that can accept any number of arguments, and not enforce the position or the
# name of the argument at "compile" time, it's possible and here's how:


def fun1(*args, **kwargs):
    print(args, kwargs)


# The * args and **kwargs parameters are special parameters that are set to a tuple and a dict, respectively:
fun1(1, 2, 3)
# Prints: (1, 2, 3) {}

fun1(a=1, b=2, c=3)
# Prints: () {'a': 1, 'b': 2, 'c': 3}

fun1('x', 'y', 'z', a=1, b=2, c=3)
# Prints: ('x', 'y', 'z') {'a': 1, 'b': 2, 'c': 3}


# If you look at enough Python code, you'll quickly discover that it is widely being used
# when passing arguments over to another function.
# For example if you want to extend the string class:

class MyString(str):
    def __init__(self, *args, **kwarg):
        print('Constructing MyString')
        super(MyString, self).__init__(*args, **kwarg)
