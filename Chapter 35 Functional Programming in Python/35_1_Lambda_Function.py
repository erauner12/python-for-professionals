

# An anonymous, inlined function defined with lambda. The parameters of the lambda are defined to the left of the
# colon. The function body is defined to the right of the colon. The result of running the function body is (implicitly)
# returned.


def s(x): return x*x
# s=lambda x:x*x


print(s(2))
