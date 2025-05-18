from collections import deque
import copy
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

virus = []
for x in range(N):
    for y in range(M):
        if table[x][y] == 2:
            virus.append([x, y])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

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