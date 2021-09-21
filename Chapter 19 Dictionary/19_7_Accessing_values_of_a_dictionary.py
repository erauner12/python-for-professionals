dictionary = {"Hello": 1234, "World": 5678}
print(dictionary["Hello"])

w = dictionary.get("whatever")
print(w)
x = dictionary.get("whatever", "nuh-uh")
print(x)
