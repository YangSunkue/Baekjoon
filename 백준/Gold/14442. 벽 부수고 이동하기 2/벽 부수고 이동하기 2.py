from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

def can_go(nx, ny):
    return 0 <= nx < N and 0 <= ny < M

def is_wall(nx, ny):
    return board[nx][ny] == '1'

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]

result = -1
queue = deque([(0, 0, 1, 0)])  # x, y, distance, broken_count
while queue:

    cx, cy, distance, broken_count = queue.popleft()

    if (cx, cy) == ((N - 1), (M - 1)):
        result = distance
        break

    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy

        if not can_go(nx, ny):
            continue

        if is_wall(nx, ny):
            if broken_count < K and not visited[nx][ny][broken_count + 1]:
                visited[nx][ny][broken_count + 1] = True
                queue.append((nx, ny, distance + 1, broken_count + 1))
        
        else:
            if not visited[nx][ny][broken_count]:
                visited[nx][ny][broken_count] = True
                queue.append((nx, ny, distance + 1, broken_count))

print(result)