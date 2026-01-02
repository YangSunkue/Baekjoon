from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[False] * (K + 1) for _ in range(M)] for _ in range(N)]

queue = deque([(0, 0, 1, 0)])  # x, y, dist, broken_count
visited[0][0][0] = True
result = -1
while queue:

    cx, cy, distance, broken_count = queue.popleft()
    is_day = (distance % 2 == 1)

    if cx == (N - 1) and cy == (M - 1):
        result = distance
        break

    add = False
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy

        if 0 > nx or N <= nx or 0 > ny or M <= ny:
            continue

        if board[nx][ny] == '1':
            if broken_count < K:
                if is_day:
                    if not visited[nx][ny][broken_count + 1]:
                        queue.append((nx, ny, distance + 1, broken_count + 1))
                        visited[nx][ny][broken_count + 1] = True
                elif not add:
                    queue.append((cx, cy, distance + 1, broken_count))
                    add = True
        
        else:
            if not visited[nx][ny][broken_count]:
                queue.append((nx, ny, distance + 1, broken_count))
                visited[nx][ny][broken_count] = True

print(result)