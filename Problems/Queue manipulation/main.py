from _collections import deque
queue = deque()
num = int(input())
for i in range(0, num):
    try:
        operation, element = input().split(" ")
        queue.append(element)
    except ValueError:
        queue.popleft()

for element in queue:
    print(element)
