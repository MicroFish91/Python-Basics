# Xargs
# numbers will hold a tuple (2, 3, 4, 5)
def multiply(*numbers):
    total = 1
    for num in numbers:
        total *= num
    return total


# Xxargs
def save_user(**user):
    print(user)


print(multiply(2, 3, 4, 5))
save_user(name="Matt", age=100, eye_color="brown")
