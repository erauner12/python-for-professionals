

# The effect of using the * operator on an argument when calling a function is that of
# unpacking the list or a tuple argument

def print_args(arg1, arg2):
    print(str(arg1) + str(arg2))


a = [1, 2]
b = tuple([3, 4])

# about to unpack the list into the argument
print_args(*a)
# 12
print_args(*b)
# 34
