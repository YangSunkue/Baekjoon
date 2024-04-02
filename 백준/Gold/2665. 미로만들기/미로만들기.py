import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
N = int(input())  # N * N의 정사각형
board = []
for _ in range(N):
    board.append(list(map(int, input().strip())))
distroy = [[INF for i in range(N)] for i in range(N)]  # 시작점부터 distroy좌표까지 오면서 부순 값을 저장한다.
visited = [[False for i in range(N)] for i in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def goingNogoing(x, y):
    if 0 <= x < N and 0 <= y < N and visited[x][y] == False:
        return True
    return False

def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0, 0))  # 부순갯수, x, y

    while queue:
        for _ in range(len(queue)):
            dist, hx, hy = heapq.heappop(queue)  # 부순갯수, x, y
            if hx == (N - 1) and hy == (N - 1):  # 도착했을 경우 ( 최소힙써서 도착했으면 무조건 최소로부순값임 )
                return dist  # 부순 갯수 리턴

            else:
                for i in range(4):  # 상하좌우 반복
                    nx = hx + dx[i]
                    ny = hy + dy[i]

                    if goingNogoing(nx, ny):
                        if board[nx][ny] == 0:  # 검은방일 때
                            cost = dist + 1  # 현재노드까지 값에 + 1한 값을 계산
                            if cost < distroy[nx][ny]:  # 그 값이 다음진행할 좌표값보다 작다면 업뎃하고 큐에 추가
                                distroy[nx][ny] = cost
                                heapq.heappush(queue, (cost, nx, ny))
                                visited[nx][ny] = True
                            
                        else:  # 하얀방일 때
                            distroy[nx][ny] = dist  # 다음 경로에 현재 부순값 넣기
                            heapq.heappush(queue, (dist, nx, ny))
                            visited[nx][ny] = True
    
print(dijkstra())