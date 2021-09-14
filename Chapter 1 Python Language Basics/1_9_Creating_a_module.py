from hello import say_hello as go
from hello import say_hello
import hello
# hello module has one function that is say_hello that prints hello!
hello.say_hello()
# module then function

say_hello()
# can import just one function

go()
# Can alias modules as variable names

if __name__ == '__main__':
    from hello import say_hello
    say_hello()
# can create stand alone runnable script
