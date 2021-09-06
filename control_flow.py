# Ternary Operator
age = 21
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)

# Chaining comparison operators
age = 22
if age >= 18 and age < 65:
    print("The OG")

if 18 <= age < 65:
    print("This works too")


# For number in range(start, stop, step)
for number in range(5, 15, 2):
    print(number)

# Iterables
for char in "Python":
    print(char)

for x in [1, 2, 3, 4]:
    print(x)

for number in range(2):
    print(number)

# For-else
successful = True
for number in range(3):
    print("Attempt", number)
    if successful:
        print("Successfully connected.")
        break
else:
    print("Request timed out...")
