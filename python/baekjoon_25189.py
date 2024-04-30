import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 맵 크기 입력받기
N, M = map(int, input().split())

# 시작, 끝 좌표 입력받기
# 문제는 1,1 부터 시작이라 1빼서 받는다
start = []
house = []
a = list(map(int, input().split()))
start.append(a[0] - 1)
start.append(a[1] - 1)
house.append(a[2] - 1)
house.append(a[3] - 1)

# 맵 입력받기
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
# 좌표별 점프횟수 저장할 테이블
jumps = [[0] * M for _ in range(N)]
# visited
visited = [[False] * M for _ in range(N)]

# 갈지 못갈지 판단하는 함수
def goingNoGoing(x, y, visited):

    # 좌표가 맵 안에 있고 아직 안 간 곳이면 갈 수 있다
    if 0 <= x < N and 0 <= y < M and visited[x][y] == False:
        return True
    return False


def frogKill():

    # 점프횟수와 시작좌표 큐에 넣고 방문체크
    # 우선순위 큐 이므로 점프횟수가 적은 곳 부터 검사한다
    queue = []
    heapq.heappush(queue, (jumps[start[0]][start[1]], start[0], start[1]))
    visited[start[0]][start[1]] = True

    while queue:

        # 점프횟수, 현재좌표 꺼내기
        jump, x, y = heapq.heappop(queue)
        # 현재좌표 먹이량
        food = board[x][y]

        # 현재 좌표가 집이라면 점프횟수 리턴
        if x == house[0] and y == house[1]:
            return jump
        # 현재 좌표가 집 좌표와 x, y중 하나라도 같다면 슈퍼점프 후 리턴 ( 점프횟수 + 1 )
        elif x == house[0] or y == house[1]:
            return jump + 1

        # 상하좌우 4방향 설정
        dx = [-food, food, 0, 0]
        dy = [0, 0, -food, food]

        # 현재좌표에서 food만큼 점프한 4방향 좌표 검사하기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 갈 수 있으면 큐에 넣기
            # 해당 좌표 점프횟수, visited 갱신
            if goingNoGoing(nx, ny, visited):
                heapq.heappush(queue, (jump + 1, nx, ny))
                jumps[nx][ny] = jump + 1
                visited[nx][ny] = True

    # 끝까지 진행했는데 집 못 갔으면
    return -1

print(frogKill())