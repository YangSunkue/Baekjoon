import sys
from collections import deque
input = sys.stdin.readline


N = int(input()) # 테스트 케이스 개수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
"""
. : 빈 공간
# : 벽
@ : 상근이 시작 위치
* : 불
"""
# 진행할지 말지 알려주는 함수
def goingNoGoing(nx, ny, who):
    
    # 불일 경우
    if who == '*':
        # tower 안에 있고 빈 공간 또는 상근이 시작 위치일때 True
        if 0 <= nx < h and 0 <= ny < w and (tower[nx][ny] == '.' or tower[nx][ny] == '@'):
            return True
        return False
    
    # 상근이일 경우
    else:
        # tower 안에 있고 아직 안 간 빈 공간일때 True
        if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == -1 and tower[nx][ny] == '.':
            return True
        return False

def fire():

    # 큐 사용
    queue = deque()
    start = []
    # 불 먼저 큐에 넣어야 함
    for i in range(h):
        for j in range(w):

            # 불 시작 위치를 큐에 삽입
            if tower[i][j] == '*':
                queue.appendleft([i, j, '*'])
            
            # 상근이 시작 위치 저장만 해두기 ( 지도에 @는 하나뿐이다 )
            if tower[i][j] == '@':
                start.append(i)
                start.append(j)

    # 상근이 시작 위치 큐에 삽입 + visited 처리
    queue.append([start[0], start[1], '.'])
    visited[start[0]][start[1]] = 0

    # bfs 시작
    while queue:
        # 큐에서 좌표 꺼내기
        x, y, who = queue.popleft()

        # 탈출 조건( 상근이가 4방향 중 어느 한쪽 끝에 도착했다면 )
        if who == '.' and (x == 0 or x == h-1 or y == 0 or y == w-1):
            return visited[x][y] + 1

        # 4방향 진행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 진행할 수 있을때
            if goingNoGoing(nx, ny, who):

                # 불이라면 진행시키고 큐에 넣기
                if who == '*':
                    tower[nx][ny] = '*'
                    queue.append([nx, ny, '*'])
                
                # 상근이라면 visited 거리 갱신하고 큐에 넣기
                else:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny, '.'])

    return 'IMPOSSIBLE'




# 테스트 케이스 N번 반복
for _ in range(N):

    # 빌딩 입력받기
    tower = []
    w, h = map(int,input().split())
    for _ in range(h):
        tower.append(list(input().strip()))

    # visited 겸 이동거리
    visited = [[-1] * w for _ in range(h)]

    print(fire())

    