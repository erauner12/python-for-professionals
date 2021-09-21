def fun1(arg1, arg2, arg3):
    return print((arg1, arg2, arg3))


# In functions, you can define a number of mandatory arguments:

# which will make the function callable only when the three arguments are given:
fun1(1, 2, 3)


# and you can define the arguments as optional, by using default values:

def fun2(arg1='a', arg2='b', arg3='c'):
    return print((arg1, arg2, arg3))


# so you can call the function in many different ways, like:
fun2(1)  # (1, b, c)
fun2(1, 2)  # (1, 2, c)
fun2(arg2=2, arg3=3)  # (a, 2, 3)


# Packing a list of arguments
# Consider you have a list of values

l = [1, 2, 3]
# You can call the function with the list of values as an argument using the * syntax:
fun1(*l)
# Returns: (1,2,3)
fun1(*['w', 't', 'f'])
# Returns: ('w','t','f')
# But if you do not provide a list which length matches the number of arguments:
# fun1(*['oops'])
# Raises: TypeError: fun1() missing 2 required positional arguments: 'arg2' and 'arg3'

print("---")
# Packing keyword arguments
# Now, you can also pack arguments using a dictionary. You can use the ** operator to tell Python to unpack the dict
# as parameter values:
d = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3
}
fun1(**d)
# Returns: (1, 2, 3)

# when the function only has positional arguments(the ones without default values) you need the dictionary to be
# contain of all the expected parameters, and have no extra parameter, or you'll get an error:

# fun1(**{'arg1': 1, 'arg2': 2})
# Raises: TypeError: fun1() missing 1 required positional argument: 'arg3'

# fun1(**{'arg1': 1, 'arg2': 2, 'arg3': 3, 'arg4': 4})
# Raises: TypeError: fun1() got an unexpected keyword argument 'arg4'

# For functions that have optional arguments, you can pack the arguments as a dictionary the same way:
fun2(**d)
# Returns: (1, 2, 3)

# But there you can omit values, as they will be replaced with the defaults:
fun2(**{'arg2': 2})
# Returns: ('a', 2, 'c')

# And the same as before, you cannot give extra values that are not existing parameters:

# fun2(**{'arg1': 1, 'arg2': 2, 'arg3': 3, 'arg4': 4})
# Raises: TypeError: fun2() got an unexpected keyword argument 'arg4'

# In real world usage, functions can have both positional and optional arguments, and it works the same:

print("---")


def fun3(arg1, arg2='b', arg3='c'):
    return print((arg1, arg2, arg3))


# you can call the function with just an iterable:
fun3(*[1])
# Returns: (1, 'b', 'c')
fun3(*[1, 2, 3])
# Returns: (1, 2, 3)


# or with just a dictionary:
fun3(**{'arg1': 1})
# Returns: (1, 'b', 'c')
fun3(**{'arg1': 1, 'arg2': 2, 'arg3': 3})
# Returns: (1, 2, 3)


# or you can use both in the same call:
fun3(*[1, 2], **{'arg3': 3})
# Returns: (1,2,3)

# Beware though that you cannot provide multiple values for the same argument:
# fun3(*[1, 2], **{'arg2': 42, 'arg3': 3})
# Raises: TypeError: fun3() got multiple values for argument 'arg2'
