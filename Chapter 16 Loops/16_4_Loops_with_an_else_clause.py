# The for and while compound statements (loops) can optionally have an else clause ( in practice, this usage is fairly rare

for i in range(3):
    print(i)
else:
    print('done')

# The else clause only executes after a for loop terminates by iterating to completion, or after a while loop
# terminates by its conditional expression becoming false

i = 0
while i < 3:
    print(i)
    i += 1
else:
    print('done')


# The else clause does not execute if the loop terminates some other way(through a break statement or by raising
# an exception):
for i in range(2):
    print(i)
    if i == 1:
        break
else:
    print('done')


# To make the else in this construct less confusing one can think of it as "if not break" or "if not found".
a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print("no exception")
