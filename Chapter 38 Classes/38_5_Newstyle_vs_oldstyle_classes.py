
# new-style class
# They inherit from the top-level object
class New(object):
    pass


# new-style instance
new = New()
new.__class__
# <class '__main__.New'>
type(new)
# <class '__main__.New'>
print(issubclass(New, object))
# True


# old-style class
class Old:
    pass


# old-style instance
old = Old()
old.__class__
# <class __main__.Old at ...>
type(old)
# <type 'instance'>
print(issubclass(Old, object))
# False


# New-style classes in Python 3 implicitly inherit from object, so there is no need to specify MyClass(object)
# anymore.

class MyClass:
    pass


my_inst = MyClass()
type(my_inst)
# <class '__main__.MyClass'>
my_inst.__class__
# <class '__main__.MyClass'>
print(issubclass(MyClass, object))
# True
