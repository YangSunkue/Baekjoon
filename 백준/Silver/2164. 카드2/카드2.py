from collections import deque
import sys
input = sys.stdin.readline

queue = deque([])
for i in range(int(input())):
    queue.append(i + 1)

while len(queue) > 1:

    queue.popleft()

    if len(queue) > 1:
        card = queue.popleft()
        queue.append(card)

print(queue.pop())