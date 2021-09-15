

# In this case, "monkey patching" means adding a new variable or method to a class after it's been defined. For
# instance, say we defined class A as


class A(object):
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return A(self.num + other.num)

    def get_num(self):
        return self.num


foo = A(42)
bar = A(6)

print(foo.get_num())  # 42
print(bar.get_num())  # 6
