from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

def can_go(nx, ny):
    return 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and maze[nx][ny] == '.'

# 불, 지훈이 시작지점 넣기
# ('불/지훈', x좌표, y좌표, 거리)
queue = deque([])
for x in range(R):
    for y in range(C):
        if maze[x][y] == 'F':
            queue.appendleft(('F', x, y, 1))  # 불을 앞에
        elif maze[x][y] == 'J':
            queue.append(('J', x, y, 1))  # 지훈이는 뒤에

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[False] * C for _ in range(R)]

result = 'IMPOSSIBLE'
while queue:
    who, cx, cy, dist = queue.popleft()

    # 지훈이가 가장자리에 도달했으면 탈출
    if who == 'J' and (cx == R - 1 or cx == 0 or cy == C - 1 or cy == 0):
        result = dist
        break

    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy

        if not can_go(nx, ny):
            continue

        if who == 'F':
            maze[nx][ny] = 'F'
            visited[nx][ny] = True
            queue.append(('F', nx, ny, dist + 1))

        elif who == 'J':
            visited[nx][ny] = True
            queue.append(('J', nx, ny, dist + 1))

print(result)