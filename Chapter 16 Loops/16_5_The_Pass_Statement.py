# pass is a null statement for when a statement is required by Python syntax(such as within the body of a for or
# while loop), but no action is required or desired by the programmer.
#
# This can be useful as a placeholder for code
# that is yet to be written.
for x in range(10):
    print(x)
    pass  # we don't want to do anything, or are not ready to do anything here, so we'll pass

x = 0
y = 1

while x == y:
    print("same")
    pass
