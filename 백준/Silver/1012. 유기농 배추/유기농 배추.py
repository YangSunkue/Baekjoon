# 실버2 -> BFS
"""
T : 테스트 케이스 개수
M : 열 ( 가로길이 )
N : 행 ( 세로길이 )
K : 심어진 배추 개수

table : 1은 배추, 2는 방문한 곳
"""
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 테이블 내에 있고, 배추인지 확인하는 함수
def going_no_going(nx, ny, table):
    if 0 <= nx < N and 0 <= ny < M and table[nx][ny] == 1:
        return True
    return False

# bfs 로직
def bfs(x, y):

    global table

    queue = deque()
    queue.append([x, y])
    table[x][y] = 2 # 방문 체크
    
    while queue:

        cx, cy = queue.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # 벌레의 전진
            if going_no_going(nx, ny, table):
                queue.append([nx, ny])
                table[nx][ny] = 2


for _ in range(T):

    M, N, K = map(int, input().split())
    table = [[0] * M for _ in range(N)]

    # 배추 위치 입력받기
    cabbage = []
    for _ in range(K):
        y, x = map(int, input().split()) # 입력값 행/열 반대라서 반대로 받는다

        table[x][y] = 1
        cabbage.append([x, y]) # 배추 위치 저장해두기

    # 모든 배추 위치 기준으로 BFS 진행
    result = 0
    for x, y in cabbage:
        if going_no_going(x, y, table):
            result += 1
            bfs(x, y)

    print(result)