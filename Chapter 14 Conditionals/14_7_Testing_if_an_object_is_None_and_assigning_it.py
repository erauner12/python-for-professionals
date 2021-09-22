# You'll often want to assign something to an object if it is None, indicating it has not been assigned. We'll use aDate.
# The simplest way to do this is to use the is None test.
from datetime import date

aDate = None

if aDate is None:
    aDate = date.today()
    print(aDate)
# But there is a more Pythonic way. The following code is also equivalent:

# This does a Short Circuit evaluation. If aDate is initialized and is not None, then it gets assigned to itself with no net
# effect. If it is None, then the datetime.date.today() gets assigned to aDate.
aDate = aDate or date.today()
print(aDate)
