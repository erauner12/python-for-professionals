
# And operator
# The and operator evaluates all expressions and returns the last expression if all expressions evaluate to True.
# Otherwise it returns the first value that evaluates to False:

print(1 and 2)
# 2
print(1 and 0)
# 0
print(1 and "Hello World")
# "Hello World"
print("" and "Pancakes")
# ""

print(1 or 2)
# 1
print(None or 1)
# 1
print(0 or [])
# []


# Lazy evaluation
def print_me():
    print('I am here!')


print(0 and print_me())
# 0


# Testing for multiple conditions
# A common mistake when checking for multiple conditions is to apply the logic incorrectly.
# This example is trying to check if two variables are each greater than 2. The statement is evaluated as - if (a) and
# (b > 2). This produces an unexpected result because bool(a) evaluates as True when a is not zero.

a = 1
b = 6
# wrong
if a and b > 2:
    print('yes')
else:
    print('no')

# yes

# Each variable needs to be compared separately.
if a > 2 and b > 2:
    print('yes')
else:
    print('no')

# no

# also
if a == 3 or a == 4 or a == 6:
    print('yes')
else:
    print('no')

# no

# Using the in operator is the canonical way to write this.

if a in (3, 4, 6):
    print('yes')
else:
    print('no')

# no
