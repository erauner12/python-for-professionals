

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book1 = Book(title="Right Ho, Jeeves", author="P.G. Wodehouse")

print(book1.title)
print(book1.author)


# print(book1.series)
# Traceback(most recent call last):
# File "<stdin>", line 1, in <module >
# AttributeError: 'Book' object has no attribute 'series'
