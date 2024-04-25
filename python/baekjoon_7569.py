from collections import deque
import sys

input = sys.stdin.readline
M, N, H = map(int, input().split())  # 가로, 세로, 높이 5, 3, 2

box = []
for i in range(N * H):  # 토마토 입력받기
    box.append(list(map(int, input().split())))
visited = [[False] * M for _ in range(N * H)]  # 방문목록 box와 똑같이 만들기

def goingNogoing(box, x, y, visited):  # 익힐수있는지 고민하는함수
    if 0 <= x < N * H and 0 <= y < M and visited[x][y] == False and box[x][y] == 0:  # 좌표가 box안에있으며 미방문이고 값이 0이어야한다
        return True
    return False

def tomato(box, visited):  # bfs
    queue = deque([])
    cnt = 0  # 안익은토마토 개수 담을 변수
    day = 0  # 다익는데 몇일걸리는지 담을 변수

    for x in range(N * H): # 0~2
        for y in range(M):  # 0~4
            if box[x][y] == 1:  # 익은 토마토를 큐에 추가
                queue.append((x, y))
                visited[x][y] = True  # 익은곳 방문체크
            elif box[x][y] == 0:  # 안익은 토마토일 경우 cnt += 1
                cnt += 1
    if cnt == 0: return 0
    
    while queue:
        for _ in range(len(queue)):  # 큐에 있는 토마토들 주변을 모두 익게 만든 뒤 날짜를 하루 추가해야 한다
            x, y = queue.popleft()  # x, y 좌표 꺼내고, 상하좌우앞뒤 전부 체크하기
            
            if goingNogoing(box, x - 1, y, visited) and x//N == (x-1)//N:  # 앞, 앞뒤는 층을 침범할 가능성이 있으므로 같은 층일때만 익힌다
                visited[x-1][y] = True  # 방문체크(익혔음)
                cnt -= 1  # 익혔으니 안익은토마토개수 -1
                queue.append((x-1, y))  # 익혔으니 큐에 넣기

            if goingNogoing(box, x + 1, y, visited) and x//N == (x+1)//N :  # 뒤, 앞뒤는 층을 침범할 가능성이 있으므로 같은 층일때만 익힌다
                visited[x+1][y] = True
                cnt -= 1
                queue.append((x+1, y))

            if goingNogoing(box, x, y - 1, visited):  # 좌
                visited[x][y-1] = True
                cnt -= 1
                queue.append((x, y-1))

            if goingNogoing(box, x, y + 1, visited):  # 우
                visited[x][y+1] = True
                cnt -= 1
                queue.append((x, y+1))
            
            if goingNogoing(box, x + N, y, visited):  # 하
                visited[x+N][y] = True
                cnt -= 1
                queue.append((x+N, y))

            if goingNogoing(box, x - N, y, visited):  # 상
                visited[x-N][y] = True
                cnt -= 1
                queue.append((x-N, y))
        day += 1 # 다익혔으면 하루 추가하기
        if cnt == 0: return day  # 하루 지날때마다 다 익었는지 검사

    if cnt == 0: return day  # 마지막에 한번 더 검사
    else: return -1

print(tomato(box, visited))