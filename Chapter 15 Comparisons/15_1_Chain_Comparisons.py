
# You can compare multiple items with multiple comparison operators with chain comparison. For example
# x > y > z

# is just a short form of:
# x > y and y > z
# This will evaluate to True only if both comparisons are True.
# The general form is
# a OP b OP c OP d ...


# As soon as one comparison returns False, the expression evaluates immediately to False, skipping all remaining
# comparisons.
# Note that the expression exp in a > exp > b will be evaluated only once, whereas in the case of
# a > exp and exp > b
# exp will be computed twice if a > exp is true.
