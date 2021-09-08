# Dictionaries
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20

if "a" in point:
    print(point["a"])

print(point.get("a"))
del point["x"]

for key in point:
    print(key, point["key"])

for key, value in point.items():
    print(key, value)


# Dictionary Comprehensions
values = {x: x * 2 for x in range(5)}

print(values)
