# Arrays can store data very compactly and are more efficient for storing large amounts of data.
# Arrays are great for numerical operations; lists cannot directly handle math operations. For
# example, you can divide each element of an array by the same number with just one line of code.

from array import array

# typecode https://docs.python.org/3/library/array.html
numbers = array("i", [1, 2, 3])
numbers.append(4)
