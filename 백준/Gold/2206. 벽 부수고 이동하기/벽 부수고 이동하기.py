from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]

def can_go(nx, ny) -> bool:
    return 0 <= nx < N and 0 <= ny < M

def is_wall(nx, ny) -> bool:
    return board[nx][ny] == '1'

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]  # visited[x][y][0]: x, y좌표에 파괴권한 가진채로 방문했는가

queue = deque([(0, 0, 1, True)])  # x, y, 이동거리, 파괴권한
result = -1
while queue:

    cx, cy, distance, distroy = queue.popleft()
    
    if (cx, cy) == (N - 1, M - 1):
        result = distance
        break

    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy

        if not can_go(nx, ny):
            continue
        
        # 벽일 경우
        if is_wall(nx, ny):
            if distroy and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                queue.append((nx, ny, distance + 1, False))
        
        # 벽 아닐 경우
        else:
            if distroy and not visited[nx][ny][0]:
                visited[nx][ny][0] = True
                queue.append((nx, ny, distance + 1, distroy))

            elif not distroy and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                queue.append((nx, ny, distance + 1, distroy))

print(result)