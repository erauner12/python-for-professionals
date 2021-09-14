# break statement
# When a break statement executes inside a loop, control flow "breaks" out of the loop immediately:
i = 0
while i < 7:
    print(i)
    if i == 4:
        print("Breaking from loop")
        break
    i += 1

print("---")
# The loop conditional will not be evaluated after the break statement is executed. Note that break statements are
# only allowed inside loops, syntactically. A break statement inside a function cannot be used to terminate loops that
# called that function.
# Executing the following prints every digit until number 4 when the break statement is met and the loop stops:


# break statements can also be used inside for loops, the other looping construct provided by Python:
for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        break

print("---")
# f a loop has an else clause, it does not execute when the loop is terminated through a break statement.
# continue statement
# A continue statement will skip to the next iteration of the loop bypassing the rest of the current block but
# continuing the loop. As with break, continue can only appear inside loops:
for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)

# Note that 2 and 4 aren't printed, this is because continue goes to the next iteration instead of continuing on to
# print(i) when i == 2 or i == 4.

print("---")
# Nested Loops
# break and continue only operate on a single level of loop. The following example will only break out of the inner
# for loop, not the outer while loop:
while True:
    for i in range(1, 5):
        if i == 2:
            # break out of the inner loop
            break  # Will only break out of the inner loop!

    # break out of the outer loop now
    break


# Python doesn't have the ability to break out of multiple levels of loop at once - - if this behavior is desired,
# refactoring one or more loops into a function and replacing break with return may be the way to go.


# Use return from within a function as a break

# The return statement exits from a function, without executing the code that comes after it.
# If you have a loop inside a function, using return from inside that loop is equivalent to having a break as the rest of
# the code of the loop is not executed(note that any code after the loop is not executed either):

def break_loop():
    for i in range(1, 5):
        if (i == 2):
            return(i)
        print(i)
    return(5)

# If you have nested loops, the return statement will break all loops:


def break_all():
    for j in range(1, 5):
        for i in range(1, 4):
            if i*j == 6:
                return(i)
        print(i*j)


"""
1  # 1*1
2  # 1*2
3  # 1*3
4  # 1*4
2  # 2*1
4  # 2*2
# return because 2*3 = 6, the remaining iterations of both loops are not executed
"""

# breaks out of single for loop and returns value it hit in the loop
break_loop()

# breaks out both of for loops
break_all()
