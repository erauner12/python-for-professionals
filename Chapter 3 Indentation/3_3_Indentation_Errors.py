# The spacing should be even and uniform throughout. Improper indentation can cause an IndentationError or
# cause the program to do something unexpected. The following example raises an IndentationError:
a = 7
if a > 5:
    print("foo")
else:
    print("bar")
print("done")

# Or if the line following a colon is not indented, an IndentationError will also be raised:
if True:
    print("true")


# If you add indentation where it doesn't belong, an IndentationError will be raised:
if True:
    a = 6
    b = 5
# If you forget to un-indent functionality could be lost. In this example None is returned instead of the expected False:


def isEven(a):
    if a % 2 == 0:
        return True
    # this next line should be even with the if
    return False


print(isEven(7))
