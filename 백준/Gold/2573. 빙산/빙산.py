from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split()) # 행, 열
ice = [list(map(int, input().split())) for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def iceBreaker():

    # 빙산을 녹이고 개수를 세는 작업이 1번의 반복
    # year는 지난 햇수
    for year in range(1, 1000000):

        # 1. 각 빙산을 얼마나 녹여야 할지 계산
        iceSub = [[0] * M for _ in range(N)]
        for x in range(1, N - 1):
            for y in range(1, M - 1):
                if ice[x][y] > 0: # 빙산일 경우

                    # 4방향 바닷물 세기
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        
                        # 바닷물일 경우 녹여야 할 높이 증가
                        if ice[nx][ny] == 0:
                            iceSub[x][y] += 1
        
        # 2. 빙산 녹이기
        for x in range(1, N - 1):
            for y in range(1, M - 1):
                if ice[x][y] > 0: # 빙산일 경우
                    ice[x][y] = max(0, ice[x][y] - iceSub[x][y]) # 녹인다, 최하 0
        
        # 3. BFS로 덩어리 세기
        visited = [[False] * M for _ in range(N)]
        cnt = 0
        for x in range(1, N - 1):
            for y in range(1, M - 1):
                if ice[x][y] > 0 and not visited[x][y]: # 방문하지 않은 빙산일 경우 BFS 진행
                    BFS(x, y, visited)
                    cnt += 1 # BFS 한번 당 덩어리 1개

                    # 2덩어리 이상이라면 즉시 year 리턴
                    if cnt > 1: return year

        # 1덩어리도 없다는 건 2덩어리가 되지 못하고 모두 녹았다는 것
        if cnt == 0: return 0

# BFS로 하나의 빙산 덩어리를 순회하며 방문체크
def BFS(sx, sy, visited):

    queue = deque()
    queue.append([sx, sy])
    visited[sx][sy] = True

    while queue:

        x, y = queue.popleft()

        # 4방향 체크
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 방문하지 않은 빙산일 경우 큐에 넣고 방문처리
            if ice[nx][ny] > 0 and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = True

print(iceBreaker())