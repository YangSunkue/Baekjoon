from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    string = sys.stdin.readline().strip()
    board.append(list(map(int, string)))

def isValidPos(x, y, N, M, visited):
    if 0 <= x < N and 0 <= y < M and board[x][y] == 1 and [x,y] not in visited:  # x,y가 board안에있고 갈수있는곳이며 아직방문하지 않은곳이어야 함
        return True
    return False

def bfs(N, M):
    queue = deque([(0,0)])  # 시작위치 삽입
    visited = [[0,0]]  # 시작위치 방문체크
    distance = 1  # 거리 초기화

    while queue:  # 큐가 빌 때까지 진행
        for _ in range(len(queue)):  # 한 노드의 인접 노드 단위로 탐색(상하좌우) 후 거리 + 1
            here = queue.popleft()
            x, y = here

            if x == N - 1 and y == M - 1:  # 현재 노드가 도착지인 경우 return
                return distance
            else:  # 도착지 아닐 경우 상하좌우 갈수있는지 탐색해서 큐에 넣고 방문처리
                if isValidPos(x - 1, y, N, M, visited): # 상
                    queue.append((x - 1, y))
                    visited.append([x - 1, y])
                if isValidPos(x + 1, y, N, M, visited): # 하
                    queue.append((x + 1, y))
                    visited.append([x + 1, y])
                if isValidPos(x, y - 1, N, M, visited): # 좌
                    queue.append((x, y - 1))
                    visited.append([x, y - 1])
                if isValidPos(x, y + 1, N, M, visited): # 우
                    queue.append((x, y + 1))
                    visited.append([x, y + 1])
        distance += 1 # 상하좌우 단위로 돈 후 거리 + 1 ( 상하좌우 다 봐도 어차피 1군데만 가니까 )

print(bfs(N, M))