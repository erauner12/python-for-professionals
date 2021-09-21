
# called a formal argument

def print_args(farg, *args):
    print("formal arg: %s" % farg)
    for arg in args:
        print("another positional arg: %s" % arg)


print_args(1, "two", 3)
# In that call, farg will be assigned as always, and the two others will be fed into the args tuple, in the order they were
# received
