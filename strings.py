# Triple quotes to format long strings
course = "Python Programming"
message = """
blah blah blah
blah
"""

# To get length of string
print(len(course))

# String slicing
print(course[0:3])
print(course[3:])
print(course[:])

# Escape character
print("Python \"Programming")

# f (formatted) strings
first_name = "Matt"
last_name = "Fisher"
print(f"{first_name} {last_name}")

# Some sample string methods
course = "   python programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("pro"))  # findIndex
print(course.replace("p", "j"))
print("pro" in course)

# Ord equivalent to .charAt()
print(ord("b"))
print(ord("B"))

# Can compare strings alphabetically
print("bag" > "apple")