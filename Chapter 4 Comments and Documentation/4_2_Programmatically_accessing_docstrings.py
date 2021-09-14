
# Docstrings are - unlike regular comments - stored as an attribute of the function they document, meaning that you
# can access them programmatically.
# An example function


def func():
    # This is a function that does nothing at all
    return


# The docstring can be accessed using the __doc__ attribute:

print(func.__doc__)


# This is a function that does nothing at all

help(func)


# Help on function func in module __main__:


func()

# This is a function that does nothing at all


def greet(name, greeting="Hello"):
    """Print a greeting to the user `name`
Optional parameter `greeting` can change what they're greeted with."""
    print("{} {}".format(greeting, name))


help(greet)
greet("Evan")


def greet(name, greeting="Hello"):
    # Print a greeting to the user `name`
    # Optional parameter `greeting` can change what they're greeted with.

    print("{} {}".format(greeting, name))


print(greet.__doc__)
