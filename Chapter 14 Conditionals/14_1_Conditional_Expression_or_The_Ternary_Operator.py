

# The ternary operator is used for inline conditional expressions. It is best used in simple, concise operations that are
# easily read.
# The order of the arguments is different from many other languages(such as C, Ruby, Java, etc.), which may
# lead to bugs when people unfamiliar with Python's "surprising" behaviour use it(they may reverse the order).
# Some find it "unwieldy", since it goes contrary to the normal flow of thought(thinking of the condition first and then the effects).


n = 5
print("Greater than 2" if n > 2 else "Smaller than or equal to 2")
# Out: 'Greater than 2'

n = 5
print("Hello" if n > 10 else "Goodbye" if n > 5 else "Good day")
