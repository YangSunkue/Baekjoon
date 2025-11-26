from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def can_go(pos):
    return 0 <= pos <= 100000 and not visited[pos]

visited = [False] * 100001
queue = deque([(N, 0)])

result = None
while queue:

    pos, dist = queue.popleft()

    if pos == K:
        result = dist
        break

    if can_go(pos + 1):
        queue.append((pos + 1, dist + 1))
        visited[pos + 1] = True
    if can_go(pos - 1):
        queue.append((pos - 1, dist + 1))
        visited[pos - 1] = True
    if can_go(pos * 2):
        queue.append((pos * 2, dist + 1))
        visited[pos * 2] = True

print(result)