from collections import deque
import copy
import sys
input = sys.stdin.readline

# 0: 빈칸, 1: 벽, 2: 바이러스
# 벽 3개를 세우는는 안전 영역 최댓값 구하기

# 백트래킹 : 벽 세우기
# 벽 3개 되면 BFS실행

# BFS : 바이러스 위치 큐에 넣고 while문 실행, 안전 영역 개수 세서 갱신하기

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# 바이러스 위치 찾기
virus = []
for x in range(N):
    for y in range(M):
        if table[x][y] == 2:
            virus.append([x, y])

def create_wall(wall):

    if wall == 3:
        bfs()
        return
    
    for x in range(N):
        for y in range(M):
            if table[x][y] == 0:
                table[x][y] = 1
                create_wall(wall + 1)
                table[x][y] = 0

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
result = 0
def bfs():
    
    global result
    
    temp_table = copy.deepcopy(table)
    queue = deque([])
    for v in virus:
        queue.append(v)

    while queue:

        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and temp_table[nx][ny] == 0:
                temp_table[nx][ny] = 2
                queue.append([nx, ny])
    
    count = 0
    for t in temp_table:
        count += t.count(0)
    result = max(result, count)

create_wall(0)
print(result)