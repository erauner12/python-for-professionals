import inspect


class A(object):
    def f(self, x):
        return 2 * x


print(A.f)

print(inspect.isfunction(A.f))
# True
print(inspect.ismethod(A.f))
# False
print(A.f(1, 7))
# Out : 14

a = A()
print(A.f(a, 20))
# Out: 40

a = A()

print(a.f)
# <bound method A.f of <__main__.A object at ...>>


print(a.f is a.f)  # False
# <bound method A.f of <__main__.A object at ...>>
print(a.f(2))
# 4
a.f = a.f
print(a.f is a.f)  # True

print("---")


# class methods and static methods – special kinds of methods.
class D(object):
    multiplier = 2  # D uses this

    @classmethod
    def f(cls, x):
        return cls.multiplier * x  # d uses this since it is an instance of the class

    @staticmethod
    def g(name):
        print("Hello, %s" % name)


# It is worth noting that at the lowest level, functions, methods, staticmethods, etc. are actually descriptors that
# invoke __get__, __set__ and optionally __del__ special methods. For more details on classmethods and
# staticmethods:


print(D.f)
# <bound method type.f of <class '__main__.D'>>
print(D.f(12))
# 24
print(D.g)
# <function D.g at ...>
D.g("world")
# Hello, world

d = D()
d.multiplier = 1337  # print the multiplier after changing it for this instance
print((D.multiplier, d.multiplier))
# (2, 1337)
print(d.f)  # <bound method D.f of <class '__main__.D'>>

print(d.f(10))  # Here we passing in a value to be multiplied by the class multiplier
# 20
