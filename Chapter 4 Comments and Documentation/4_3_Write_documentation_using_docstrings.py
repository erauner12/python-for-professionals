# A docstring is a multi-line comment used to document modules, classes, functions and methods. It has to be the
# first statement of the component it describes.


def hello(name):
    """Greet someone.
    Print a greeting ("Hello") for the person with the given name.
    """
    print("Hello "+name)


class Greeter:
    """
    An object used to greet people.
    It contains multiple greeting functions for several languages
    and times of the day.
    """


# According to PEP 257, they should be used with short and simple functions. Everything is placed in one line, e.g:
def hello():
    """Say hello to your friends."""


print("Hello my friends!")

# The docstring shall end with a period, the verb should be in the imperative form.
# Multi-line Docstrings:
# Multi-line docstring should be used for longer, more complex functions, modules or classes.

# Sphinx


def hello(name, greeting, language="en"):
    """Say hello to a person.
       :param name: the name of the person
       :type name: str
       :param language: the language in which the person should be greeted
       :type language: str
       :return: a number
       :rtype: int
       """
    pass

# Google


def hello(name, language="en"):
    """Say hello to a person.

    Args:
        name: the name of the person as string
        language: the language code string
    Returns:
        A number.
    """
