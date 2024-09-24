# BFS, 백트래킹
# 백트래킹으로 벽 3개를 세우는 경우의 수를 전부 구한 후, BFS로 바이러스를 전파시킨 후 안전 영역의 개수를 센다
from collections import deque
import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split()) # 행, 열
graph = [] # 지도
for _ in range(N):
    graph.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 3개의 벽을 세우는 경우의 수를 구하는 함수
def createWall(wall):

    if wall == 3: # 벽 3개가 세워졌다면 안전영역 개수 센다
        BFS()
        return
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0: # 안전 영역일 경우 벽을 세운다
                graph[i][j] = 1
                createWall(wall + 1) # 벽 개수 1개 추가하고 탐색
                graph[i][j] = 0 # 갔다 왔으니 다시 벽 허물어 준다


result = 0 # 결과 담을 변수
# BFS로 바이러스를 퍼트린 후 안전 영역 개수를 세는 함수
def BFS():

    global result

    trashGraph = copy.deepcopy(graph)
    queue = deque()

    for i in range(N):
        for j in range(M):
            if trashGraph[i][j] == 2: # 바이러스일 경우 큐에 추가
                queue.append([i, j])

    while queue:
        x, y = queue.popleft()

        # 상하좌우 퍼뜨리기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 좌표가 지도 안에 있고 안전 영역일 경우 퍼뜨린다
            if 0 <= nx < N and 0 <= ny < M and trashGraph[nx][ny] == 0:
                trashGraph[nx][ny] = 2
                queue.append([nx, ny])

    # 다 퍼뜨렸으면 안전영역 개수 센다
    cnt = 0
    for g in trashGraph:
        cnt += g.count(0)
    
    # 더 큰 값을 결과값으로 갱신한다
    result = max(result, cnt)

createWall(0)
print(result)