
foo = True
bar = True

if foo:
    if bar:
        x = 42
else:
    print(foo)

# <if > <foo > <: > [0]
# <INDENT > <if > <bar > <: > [0, 4]
# <INDENT > <x > <= > <42 > [0, 4, 8]
# <DEDENT > <DEDENT > <else > <: > [0]
# <INDENT > <print > <foo > [0, 2]
# <DEDENT >
