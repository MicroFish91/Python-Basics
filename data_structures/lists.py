# Combining and creating lists
letters = ["a", "b", "c"]
zeros = [0] * 5
print(zeros + letters)

# Converting iterables to a list
numbers = list(range(10))
print(numbers)

# Similar slicing capabilities to string slicing

# List unpacking (much like JS Destructuring)
numbers = [1, 2, 3]
first, second, third = numbers
print(first, second, third)

# Interesting unpacking cases
numbers = [1, 2, 3, 4, 4, 4, 4, 9]
first, second, *other = numbers
first, *other, last = numbers

# Enumerate --> instead of a value, gives a tuple (key, value)
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)

# Add
letters.append("d")
letters.insert(0, "-")

# Remove
letters.pop()
letters.pop(0)
letters.remove("b")  # removes the first occurrence only
del letters[0:3]
letters.clear()  # delete all elements of the list

# Finding Items
# equivalent to .indexOf => returns an error instead of -1 if doesn't exist
if "d" in letters:
    print(letters.index("d"))

print(letters.count("d"))

# Sorting
# .sort modifies in place
numbers = [3, 51, 2, 8, 6]
numbers.sort()
# numbers.sort(reverse=True)
print(numbers)

# sorted() returns a new list

# Lambda (anonymous) functions
# items.sort(key=lambda parameters:expression)
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]

# items.sort(key=lambda item: item[1])

# Map & Filter
prices = list(map(lambda item: item[1], items))
filtered = list(filter(lambda item: item[1] >= 10, items))

# Refactoring with List Comprehensions
# [expression for item in items]
prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]

# Zip function => creates a list of tuples
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2)))  # [(1, 10), (2, 20), (3, 30)]
print(list(zip("abc", list1, list2)))


# Tuple is a read-only list
point = (1, 2, 3)
point = (1,)
point = ()
point = point[0:2]
# point = tuple(iterable)


# Swapping values
x = 10
y = 11

x, y = y, x