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
queue = deque([(0, 0, 1, 0)])  # (x, y, 거리, 부순개수)
visited[0][0][0] = True
while queue:

    cx, cy, distance, broken_count = queue.popleft()
    is_daytime = (distance % 2 == 1)

    if (cx, cy) == ((N - 1), (M - 1)):
        result = distance
        break

    add = False
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy

        if not can_go(nx, ny):
            continue
        
        # 벽
        if is_wall(nx, ny):
            if broken_count < K:
                if is_daytime:
                    if not visited[nx][ny][broken_count + 1]:
                        visited[nx][ny][broken_count + 1] = True
                        queue.append((nx, ny, distance + 1, broken_count + 1))
                elif not add:
                    add = True
                    queue.append((cx, cy, distance + 1, broken_count))
        # 벽이 아님
        else:
            if not visited[nx][ny][broken_count]:
                visited[nx][ny][broken_count] = True
                queue.append((nx, ny, distance + 1, broken_count))

print(result)