
# For the sake of data encapsulation, sometimes you want to have an attribute which value comes from other
# attributes or, in general, which value shall be computed at the moment. The standard way to deal with this situation
# is to create a method, called getter or a setter.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


# In the example above, it's easy to see what happens if we create a new Book that contains a title and a author. If all
# books we're to add to our Library have authors and titles,
#
# then we can skip the getters and setters and use the dot
# notation.
#
# However, suppose we have some books that do not have an author and we want to set the author to
# "Unknown". Or if they have multiple authors and we plan to return a list of authors.
# In this case we can create a getter and a setter for the author attribute.

class P:
    def __init__(self, title, author):
        self.title = title
        self.setAuthor(author)

    def get_author(self):
        return self.author

    def set_author(self, author):
        if not author:
            self.author = "Unknown"
        else:
            self.author = author


# This scheme is not recommended.
# One reason is that there is a catch: Let's assume we have designed our class with the public attribute and no
# methods. People have already used it a lot and they have written code like this:

# book = Book(title="Ancient Manuscript", author="Some Guy")
# book.author = ""  # Cos Some Guy didn't write this one!

# Now we have a problem. Because author is not an attribute! Python offers a solution to this problem called
# properties. A method to get properties is decorated with the @ property before it's header. The method that we
# want to function as a setter is decorated with @ attributeName.setter before it.
# Keeping this in mind, we now have our new updated class.


# This dow not work
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

        @property
        def author(self):
            return self.__author

        @author.setter
        def author(self, val):
            if author:
                self.author = "Unknown"
            else:
                self.author = author


# Note, normally Python doesn't allow you to have multiple methods with the same name and different number of
# parameters. However, in this case Python allows this because of the decorators used.
# If we test the code:

book = Book(title="Ancient Manuscript", author="Some Guy")


book.author = ""  # Cos Some Guy didn't write this one!
print(type(book.author))
print(book.title)
print(book.author)


class OurClass:
    def __init__(self, a):
        self.OurAtt = a

    @property
    def OurAtt(self):
        return self.__OurAtt

    @OurAtt.setter
    def OurAtt(self, val):
        if val < 0:
            self.__OurAtt = 0
        elif val > 1000:
            self.__OurAtt = 1000
        else:
            self.__OurAtt = val


x = OurClass(1001)
print(x.OurAtt)
