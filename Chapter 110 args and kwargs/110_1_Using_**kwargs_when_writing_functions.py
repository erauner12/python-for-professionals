
# You can define a function that takes an arbitrary number of keyword(named) arguments by using the double star
# ** before a parameter name:


def print_kwargs(**kwargs):
    print(kwargs)


# When calling the method, Python will construct a dictionary of all keyword arguments and make it available in the
# function body:
print_kwargs(a="two", b=3)
# prints: "{a: "two", b=3}"

# Note that the ** kwargs parameter in the function definition must always be the last parameter, and it will only
# match the arguments that were passed in after the previous ones.


def example(a, **kw):
    print(kw)


example(a=2, b=3, c=4)  # => {'b': 3, 'c': 4}


# Inside the function body, kwargs is manipulated in the same way as a dictionary
# in order to access individual
# elements in kwargs you just loop through them as you would with a normal dictionary:

def print_kwargs(**kwargs):
    for key in kwargs:
        print("key = {0}, value = {1}".format(key, kwargs[key]))


print_kwargs(a="two", b=1)
# Out:
# key = a, value = "two"
# key = b, value = 1
