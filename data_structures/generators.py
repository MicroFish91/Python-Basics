# can be used to iterate over a large number of values, without creating a massive list

from sys import getsizeof

values = (x * 2 for x in range(1000000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(1000000)]
print("list:", getsizeof(values))
