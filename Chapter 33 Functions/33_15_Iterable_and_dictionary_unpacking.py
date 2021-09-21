# Functions allow you to specify these types of parameters: positional, named, variable positional, Keyword args
# (kwargs). Here is a clear and concise use of each type.


def unpacking(a, b, c=45, d=60, *args, **kwargs):
    print(a, b, c, d, args, kwargs)


unpacking(1, 2)
# 1 2 45 60 () {}

unpacking(1, 2, 3, 4)
# 1 2 3 4 () {}

unpacking(1, 2, c=3, d=4)
# 1 2 3 4 () {}

unpacking(1, 2, d=4, c=3)
# 1 2 3 4 () {}

unpacking(1, 2, d=4, c=3)
# 1 2 3 4 () {}

print("---")
pair = (3, )

unpacking(1, 2, *pair, d=4)
# 1 2 3 4 () {}

unpacking(1, 2, d=4, *pair)
# 1 2 3 4 () {}

# will fail
# unpacking(1, 2, *pair, c=3)
# unpacking(1, 2, c=3, *pair)

print("---")
args_list = [3]
unpacking(1, 2, *args_list, d=4)
# 1 2 3 4 () {}

unpacking(1, 2, d=4, *args_list)
# 1 2 3 4 () {}

# will fail
unpacking(1, 2, C=3, *args_list)
# 1 2 3 60 () {'C': 3}

unpacking(1, 2, *args_list, C=3)
# 1 2 3 60 () {'C': 3}

print("---")
args_list = [3]

unpacking(1, 2, *args_list, d=4)
# 1 2 3 4 () {}

unpacking(1, 2, d=4, *args_list)
# 1 2 3 4 () {}

unpacking(1, 2, C=3, *args_list)
# 1 2 3 60 () {'C': 3}

unpacking(1, 2, *args_list, C=3)
# 1 2 3 60 () {'C': 3}

print("---")
args_list = [3, 4]

unpacking(1, 2, *args_list)
# 1 2 3 4 () {}

unpacking(1, 2, 3, 4, *args_list)
# 1 2 3 4 (3, 4) {}

# will fail
# unpacking(1, 2, d=4, *args_list)
# unpacking(1, 2, *args_list, d=4)

print("---")
arg_dict = {'c': 3, 'd': 4}
unpacking(1, 2, **arg_dict)
# 1 2 3 4 () {}

arg_dict = {'d': 4, 'c': 3}
unpacking(1, 2, **arg_dict)
# 1 2 3 4 () {}

arg_dict = {'c': 3, 'd': 4, 'not_a_parameter': 75}
unpacking(1, 2, **arg_dict)
# 1 2 3 4 () {'not_a_parameter': 75}


# unpacking(1, 2, *pair, **arg_dict)

# unpacking(1, 2, 3, 4, **arg_dict)

# Positional arguments take priority over any other form of argument passing
# unpacking(1, 2, **arg_dict, c=3)

# unpacking(1, 2, 3, **arg_dict, c=3)
