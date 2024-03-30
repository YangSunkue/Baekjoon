from collections import deque
import sys

def isValidPos(x, y, N, M, visited):  # 갈 수 있는지 확인하는 함수
    if 0 <= x < N and 0 <= y < M and board[x][y] == 1 and [x,y] not in visited:
        return True
    return False

def bfs(N, M):
    queue = deque([(0,0)])  # 시작위치 큐에 삽입
    visited = [[0,0]]
    distance = 1

    while queue:  # 큐가 빌 때까지 진행한다
        size = len(queue)
        for _ in range(size):
            here = queue.popleft()
            x, y = here  # ex) 0,0

            if x == N - 1 and y == M - 1:  # 현재위치가 도착지일 경우 반복 종료
                return distance
            # 상하좌우 모두 검사
            if isValidPos(x - 1, y, N, M, visited):
                queue.append((x - 1, y)) # 상
                visited.append([x - 1, y])
            if isValidPos(x + 1, y, N, M, visited):
                queue.append((x + 1, y)) # 하
                visited.append([x + 1, y])
            if isValidPos(x, y - 1, N, M, visited):
                queue.append((x, y - 1)) # 좌
                visited.append([x, y - 1])
            if isValidPos(x, y + 1, N, M, visited):
                queue.append((x, y + 1)) # 우
                visited.append([x, y + 1])
        distance += 1
    return -1

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    string = sys.stdin.readline().strip()
    board.append(list(map(int, string)))
    
result = bfs(N, M)
print(result)