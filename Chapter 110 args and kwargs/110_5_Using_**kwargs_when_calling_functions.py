# You can use a dictionary to assign values to the function's parameters
# using parameters name as keys in the
# dictionary and the value of these arguments bound to each key:


def test_func(arg1, arg2, arg3):  # Usual function with three arguments
    print("arg1: %s" % arg1)
    print("arg2: %s" % arg2)
    print("arg3: %s" % arg3)


# Note that dictionaries are unordered, so we can switch arg2 and arg3. Only the names matter.
kwargs = {"arg3": 3, "arg2": "two"}
# Bind the first argument (ie. arg1) to 1, and use the kwargs dictionary to bind the others
test_func(1, **kwargs)
