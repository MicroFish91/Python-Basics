# Sets
# Unoredered list, cannot access them using indices
numbers = [1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# Union
print(first | second)

# Intersection
print(first & second)

# Difference
print(first - second)

# Symmetric Difference
print(first ^ second)

if 1 in first:
    print("yes")


second.add(6)
second.remove(6)
