# To use default values with **kwargs

def fun(**kwargs):
    # if the key does not exist, will default to 0
    print(kwargs.get('value', 0))


fun()
# print 0
fun(value=1)
