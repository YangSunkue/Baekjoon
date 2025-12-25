from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

"""
하루 지나면 익토 상하좌우 전파
최소 며칠이 지나면 다 익는지 계산

0: 안익토
1: 익토
-1: 없음
"""
def can_go(nx, ny) -> bool:
    return 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0

goal = N * M  # 최종 목표 익은 토마토 개수
count = 0  # 현재 익은 토마토 개수

# 익은 토마토를 전부 큐에 넣고 BFS
queue = deque([])  # (x, y, 일수)
for x in range(N):
    for y in range(M):
        if box[x][y] == 1:
            queue.append((x, y, 0))
            count += 1
        elif box[x][y] == -1:
            goal -= 1
result = 0
while queue:
    cx, cy, day = queue.popleft()
    result = max(result, day)

    # 4방향 진행
    for dx, dy in directions:
        nx, ny = cx + dx, cy + dy

        if not can_go(nx, ny):
            continue

        box[nx][ny] = 1
        count += 1
        queue.append((nx, ny, day + 1))

print(result) if count == goal else print(-1)