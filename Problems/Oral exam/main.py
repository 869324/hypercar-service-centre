from _collections import deque

queue = deque()
num = int(input())
for i in range(0, num):
    str = input()
    try:
        status, name = str.split()
        queue.append(name)
    except ValueError:
        if str == "PASSED":
            print(queue.popleft())
        else:
            queue.append(queue.popleft())
