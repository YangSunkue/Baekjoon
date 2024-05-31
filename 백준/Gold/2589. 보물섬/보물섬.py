from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(input().strip()))

def createVisited():
    return [[0] * M for _ in range(N)]

def goingNoGoing(nx, ny, visited):

    # maps 안에 좌표가 있고, 육지이고, 방문하지 않았으면 True 리턴
    if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 'L' and visited[nx][ny] == 0:
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):

    queue = deque()
    queue.append((i, j))

    visited = createVisited()
    visited[i][j] = 1

    count = 0

    while queue:
        x, y = queue.popleft()

        # 상하좌우 4방향에 대하여 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 갈 수 있는 곳일 경우
            if goingNoGoing(nx, ny, visited):
                visited[nx][ny] = visited[x][y] + 1
                count = max(count, visited[nx][ny])  # 최대 거리 갱신
                queue.append((nx, ny))  # 큐에 넣기

    # 시작 지점 값 1부터 시작했으므로, 1을 뺀 값을 return 한다
    return count - 1

result = 0

for i in range(N):
    for j in range(M):
        # 모든 육지 좌표에 대하여 bfs 진행
        if maps[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)