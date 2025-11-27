from collections import deque
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

def is_valid(num):
    return num <= B

result = -1
queue = deque([(A, 1)])
while queue:

    num, dist = queue.popleft()
    if num == B:
        result = dist
        break

    if is_valid(num * 2):
        queue.append((num * 2, dist + 1))
    if is_valid(int(str(num) + '1')):
        queue.append((int(str(num) + '1'), dist + 1))

print(result)