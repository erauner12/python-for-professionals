
class C:
    x = 2  # class variable

    def __init__(self, y):
        self.y = y  # instance variable


c1 = C(3)
print(c1.x)
# 2
print(c1.y)
# 3
print("---")

c2 = C(4)
print(c2.x)
# 2
print(c2.y)

print("---")

# Note that mutating class variables from instances can lead to some unexpected consequences.


class D:
    x = []

    def __init__(self, item):
        self.x.append(item)  # note that this is not an assignment!


d1 = D(1)
d2 = D(2)
print(d1.x)
# [1, 2]
print(d2.x)
# [1, 2]
print(D.x)  # the global variables changes as well
# [1, 2]
