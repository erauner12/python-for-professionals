# Python 3 allows you to define function arguments which can only be assigned by keyword, even without default
# values. This is done by using star * to consume additional positional parameters without setting the keyword
# parameters. All arguments after the * are keyword-only(i.e. non-positional) arguments. Note that if keyword-only
# arguments aren't given a default, they are still required when calling the function.

def print_args(arg1, *args, keyword_required, keyword_only=True):
    print("first positional arg: {}".format(arg1))
    for arg in args:
        print("another positional arg: {}".format(arg))
    print("keyword_required value: {}".format(keyword_required))
    print("keyword_only value: {}".format(keyword_only))


# TypeError: print_args() missing 1 required keyword-only argument:
# print_args(1, 2, 3, 4)
# 'keyword_required'

print_args(1, 2, 3, keyword_required=4)
print("---")
print_args(1, 2, 3, keyword_required=4, keyword_only=False)
# first positional arg: 1
# another positional arg: 2
# another positional arg: 3
# keyword_required value: 4
# keyword_only value: True
