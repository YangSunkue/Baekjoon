from collections import deque
import sys

input = sys.stdin.readline

R, C = map(int, input().split())
forest = []
for _ in range(R):
    forest.append(list(input().strip()))
visited = [[-1 for _ in range(C)] for i in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()

for x in range(R):
    for y in range(C):
        if forest[x][y] == '*':
            queue.appendleft((x, y))
        elif forest[x][y] == 'S':
            queue.append((x, y))
            visited[x][y] = 0

def goingNogoing(x, y, forest, visited, who):
    if 0 <= x < R and 0 <= y < C and forest[x][y] != '*' and forest[x][y] != 'X' and visited[x][y] == -1:
        if who == '*':
            if forest[x][y] != 'D':
                return True
        else:
            return True
    return False

def killDochi():
    while queue:
        x, y = queue.popleft()
        who = forest[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if goingNogoing(nx, ny, forest, visited, who):
                if forest[nx][ny] == 'D':
                    return visited[x][y] + 1
                
                visited[nx][ny] = visited[x][y] + 1
                forest[nx][ny] = who
                queue.append((nx, ny))
    
    return "KAKTUS"

print(killDochi())