# 도치가 사방으로 가는 것과, 물이 도치의 방문목록에 영향을 받는 것(도치가 지나간 길 안가는것)은 결과에 영향을 미치지 않는다.
import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())  # 행, 열
forest = [list(input().strip()) for _ in range(R)]
visited = [[-1] * C for _ in range(R)]  # -1로 설정해두고 도치의 이동 과정을 입력할것이다


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque()
for x in range(R):
    for y in range(C):
        if forest[x][y] == '*':  # 물 좌표를 큐의 앞에 추가 ( 물이 먼저 가야 한다 )
            queue.appendleft((x, y))
        elif forest[x][y] == 'S': # 도치 좌표를 추가
            queue.append((x, y))
            visited[x][y] = 0  # 출발점에 걸린 시간 0 저장 -> 1씩 증가시키며 진행할것

def goingNogoing(x, y, visited, forest, who): # 갈지말지 판단하는 함수
    if 0 <= x < R and 0 <= y < C and visited[x][y] == -1 and forest[x][y] != 'X' and forest[x][y] != '*':
        if who == '*': # 물이면 다음곳이 비버집이면 안됨
            if forest[x][y] != 'D':
                return True
        else:
            return True
    return False

def dochiKill():
    while queue:
        x, y = queue.popleft() # 물부터 나옴
        who = forest[x][y]  # 현재위치. 물 또는 도치가 들어있다.

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i] # 상하좌우로 반복해준다

            if goingNogoing(nx, ny, visited, forest, who):  # 갈수 있다면
                if forest[nx][ny] == 'D':  # 비버집 도착했으면 결과 출력
                    return visited[x][y] + 1
                
                visited[nx][ny] = visited[x][y] + 1  # 다음 진출경로에 시간 입력
                forest[nx][ny] = who  # 다음 칸을 도치/물로 변경 (진출한다)
                queue.append((nx, ny))

    return "KAKTUS"  # 숲을 다 돌았는데 비버집에 못 갔다면 KAKTUS 리턴

print(dochiKill())