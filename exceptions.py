from timeit import timeit

# Raising exceptions has a large time cost, in larger, scaled
# applications, only use as necessary

#  with will call automatically release external resources
# without expclicitly calling the finally block
# __ magic methods enter/exit support content management protocol
# and can be used with the "with" statement
try:
    # file = open("app.py")
    # with open("app.py") as file:
    #     print("file opened")
    age = int(input("Age: "))
    xFactor = 10 / age
except (ValueError, ZeroDivisionError) as ex:
    print("You didn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
# finally:
# file.close()


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age

try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

print("first code=", timeit(code1, number=10000))
print("second code=", timeit(code2, number=10000))
