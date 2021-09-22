# The following values are considered falsey, in that they evaluate to False when applied to a boolean operator.

testVar = None
testVar = False
testVar = 0  # or any numerical value equivalent to zero, for example 0L, 0.0, 0j
testVar = ''
testVar = ""
testVar = ()
testVar = []
testVar = {}
# User-defined types where the __bool__ or __len__ methods return 0 or False


# All other values in Python evaluate to True.
