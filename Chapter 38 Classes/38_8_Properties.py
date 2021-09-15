

# Python classes support properties, which look like regular object variables, but with the possibility of attaching
# custom behavior and documentation.

class MyClass(object):
    def __init__(self):
        self._my_string = ""
        self._my_second_string = "test"

    @property
    def string(self):
        """A profoundly important string."""
        return self._my_string

    @string.setter
    def string(self, new_value):
        assert isinstance(new_value, str), \
            "Give me a string, not a %r!" % type(new_value)
        self._my_string = new_value

    @string.deleter
    def x(self):
        self._my_string = None
        # self.__dict__["_my_string"] = None


mc = MyClass()
mc.string = "String!"
print(mc.string)
print(mc.__dict__)
mc._my_string = "Changed String!"

print(mc.string)


print("---")


class Character(object):

    def __init__(self, name, max_hp):
        self._name = name
        self._hp = max_hp
        self._max_hp = max_hp

    # Max hp was missing
    @property
    def max_hp(self):
        return self._max_hp

    # Make hp read only by not providing a set method
    @property
    def hp(self):
        return self._hp

    # had to add this
    @hp.setter
    def hp(self, healthPoints):
        self._hp = healthPoints

    # Make name read only by not providing a set method
    @property
    def name(self):
        return self.name

    @property
    def is_alive(self):
        return self.hp != 0

    @property
    def is_wounded(self):
        return self.hp < self.max_hp if self.hp > 0 else False

    @property
    def is_dead(self):
        return not self.is_alive

    def take_damage(self, damage):
        self.hp -= damage
        self.hp = 0 if self.hp < 0 else self.hp

    def take_potion(self, regen):
        self.hp += regen
        # would want to do something here to take account for max_hp


bilbo = Character("Bilbo Baggins", 100)
print(bilbo.hp)
# out : 100

# bilbo.hp = 200
# out : AttributeError: can't set attribute

# hp attribute is read only.
print(bilbo.is_alive)
# out : True
print(bilbo.is_wounded)
# out : False
print(bilbo.is_dead)
# out : False
print(bilbo.hp)

bilbo.take_damage(50)
bilbo.take_potion(20)
print(bilbo.hp)
# out : 50
print(bilbo.is_alive)
# out : True
print(bilbo.is_wounded)
# out : True
print(bilbo.is_dead)
# out : False

bilbo.take_damage(50)
# bilbo.take_damage(20) # this will kill bilbo

print(bilbo.hp)
# out : 0
print(bilbo.is_alive)
# out : False
print(bilbo.is_wounded)
# out : False
print(bilbo.is_dead)
# out : True
