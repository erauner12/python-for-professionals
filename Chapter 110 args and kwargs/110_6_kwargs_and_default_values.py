# To use default values with **kwargs

def fun(**kwargs):
    print(kwargs.get('value', 0))


fun()
# print 0
fun(value=1)
