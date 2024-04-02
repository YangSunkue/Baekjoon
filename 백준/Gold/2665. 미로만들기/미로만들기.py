import heapq
import sys

INF = int(1e9)
input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):  # 미로 입력받기
    board.append(list(map(int, input().strip())))
distroy = [[INF for _ in range(N)] for _ in range(N)]  # 부순갯수
visited = [[False for _ in range(N)] for _ in range(N)]  # 방문목록

def goingNogoing(x, y):  # 갈지말지 정하는함수
    if 0 <= x < N and 0 <= y < N and visited[x][y] == False:
        return True
    return False

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def dijkstra():
    queue = []
    heapq.heappush(queue, (0, 0, 0))  # 부순갯수, x, y
    visited[0][0] = True
    distroy[0][0] = 0

    while queue:
        for _ in range(len(queue)):
            dist, cx, cy = heapq.heappop(queue)  # 큐에서 현재까지 부순갯수, x, y 빼기
            if cx == N - 1 and cy == N - 1:  # 도착했다면 부순갯수 리턴
                return dist
            
            for i in range(4):  # 상하좌우 반복
                nx = cx + dx[i]
                ny = cy + dy[i]

                if goingNogoing(nx, ny):
                    if board[nx][ny] == 0:  # 다음방이 검은방이면
                        cost = dist + 1  
                        distroy[nx][ny] = cost  # 부순갯수 +1 해서 테이블 갱신
                        heapq.heappush(queue, (cost, nx, ny))  # 갱신했으니 큐에 넣기
                        visited[nx][ny] = True  # 방문체크
                    else:
                        distroy[nx][ny] = dist  # 부순갯수 그대로 테이블 갱신
                        heapq.heappush(queue, (dist, nx, ny))  # 갱신했으니 큐에 넣기
                        visited[nx][ny] = True  # 방문체크

print(dijkstra())