class Person(object):
    """A simple class."""  # docstring
    species = "Homo Sapiens"  # class attribute

    def __init__(self, name):  # special method
        """This is the initializer. It's a special
        method (see below).
        """
        self.name = name  # instance attribute

    def __str__(self):  # special method
        """This method is run when Python tries
        to cast the object to a string. Return
        this string when using print(), etc.
        """
        return self.name

    def rename(self, renamed):  # regular method
        """Reassign and print the name attribute."""
        self.name = renamed
        print("Now my name is {}".format(self.name))


kelly = Person("Kelly")
joseph = Person("Joseph")
john_doe = Person("John Doe")

# Attributes
kelly.species = 'Homo Sapiens'
john_doe.species = 'Homo Sapiens'
joseph.species = 'Homo Sapiens'
kelly.name = 'Kelly'
joseph.name = 'Joseph'

print(john_doe.__str__())
print(john_doe)
john_doe.rename("John")
print(john_doe)
