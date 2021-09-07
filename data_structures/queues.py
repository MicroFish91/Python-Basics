# Queues - FIFO (First in first out)
# Normally expensive to pop off front of large lists O(n)

# Deque (double ended queue) is preferred over list in the cases where we need quicker append
# and pop operations from both the ends of container, as deque provides an O(1)
# time complexity for append and pop operations as compared to lists which provide
# O(n) time complexity.

from collections import deque

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
