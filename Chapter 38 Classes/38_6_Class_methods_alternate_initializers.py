class Person(object):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")


# Wrong

#  two main problems with this bit of code:

# The parameters first_name and last_name are now misleading, since you can enter a full name for
# first_name. Also, if there are more cases and / or more parameters that have this kind of flexibility, the
# if/elif/else branching can get annoying fast.

# 2. Not quite as important, but still worth pointing out: what if last_name is None, but first_name doesn't split
# into two or more things via spaces? We have yet another layer of input validation and / or exception
# handling...

# class Person(object):
#     def __init__(self, first_name, age, last_name=None):
#         if last_name is None:
#             self.first_name, self.last_name = first_name.split(" ", 2)
#         else:
#             self.first_name = first_name
#             self.last_name = last_name

#         self.full_name = self.first_name + " " + self.last_name
#         self.age = age

#         def greet(self):
#             print("Hello, my name is " + self.full_name + ".")

class Person(object):

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.full_name = first_name + " " + last_name

    @classmethod
    def from_full_name(cls, name, age):
        if " " not in name:
            raise ValueError
        first_name, last_name = name.split(" ", 2)
        return cls(first_name, last_name, age)

    def greet(self):
        print("Hello, my name is " + self.full_name + ".")


bob = Person("Bob", "Bobberson", 42)
alice = Person.from_full_name("Alice Henderson", 31)
bob.greet()
alice.greet()
