from collections import deque
import sys
import copy

N, M = map(int, input().split()) # 행, 열
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스 위치 미리 찾아놓기
virus = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append([i, j])


# 벽 3개를 세우는 모든 경우의 수를 구하기
# 경우의 수 마다 바이러스를 전파시킨 후 안전영역 개수 세기

def createWall(wall):
    
    if wall == 3:
        BFS()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                createWall(wall + 1)
                graph[i][j] = 0

result = 0
def BFS():

    global result
    trashGraph = copy.deepcopy(graph)
    queue = deque()
    for v in virus:
        queue.append(v)

    while queue:
        
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and trashGraph[nx][ny] == 0:
                trashGraph[nx][ny] = 2
                queue.append([nx, ny])
    
    cnt = 0
    for g in trashGraph:
        cnt += g.count(0)
    result = max(result, cnt)

createWall(0)
print(result)
