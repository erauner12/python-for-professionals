car = {}
car["wheels"] = 4
car["color"] = "Red"
car["model"] = "Corvette"


print("Little " + car["color"] + " " + car["model"] + "!")
# This would print out "Little Red Corvette!"

car = {"wheels": 4, "color": "Red", "model": "Corvette"}

for key in car:
    print(key + ": " + str(car[key]))
# wheels: 4
# color: Red
# model: Corvette
