# DFS, 백트래킹
import sys
input = sys.stdin.readline

# 입력받기
R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input().strip()))

# 사전준비
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
visited = [[False] * C for _ in range(R)]
visited[0][0] = True
path = set() # 집합으로 불필요한 중복 알파벳이 들어가는 것을 방지
result = 1

# DFS로 모든 경로의 깊이를 탐색후 최대 깊이 갱신하는 함수
def backTracking(x, y, depth):

    global result
    path.add(board[x][y]) # 경로에 알파벳 추가
    result = max(result, depth) # 최댓값 갱신

    # 4방향 체크
    for di in directions:
        nx, ny = x + di[0], y + di[1]
        
        # 갈수있으면 재귀
        if goingNoGoing(nx, ny):
            visited[nx][ny] = True
            backTracking(nx, ny, depth + 1)
            visited[nx][ny] = False
    
    path.remove(board[x][y]) # 돌아가기 전 경로에서 알파벳 빼주기

# 다음 좌표가 유효한지 확인하는 함수
def goingNoGoing(nx, ny):
    # board안에 있고, 겹치는 알파벳 아니고, 아직 방문 안했을 경우 True
    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] not in path and not visited[nx][ny]:
        return True
    return False

# 정답 출력
backTracking(0, 0, 1)
print(result)