# 구현, 시뮬레이션
import sys
input = sys.stdin.readline

# 입력받기
N, M = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 0, 1, 2, 3 -> 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소 시작
room[x][y] = 2
result = 1
def cleaner(x, y, d):

    global result

    # 무한루프 방지를 위한 for문
    for _ in range(50**3):
        clean = False # 청소여부

        # 4방향 탐색
        for _ in range(4):
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            # 미청소 구역일 경우 전진
            if room[nx][ny] == 0:
                clean = True
                room[nx][ny] = 2
                result += 1
                x, y = nx, ny
                break
        
        # 4방향 갈곳이 없으면 후진 ( 방향 유지 )
        if not clean:
            tmpDir = (d + 2) % 4
            nx = x + dx[tmpDir]
            ny = y + dy[tmpDir]
        
        # 후진했는데 벽이라면 종료
        if room[nx][ny] == 1:
            return
        else:
            x, y = nx, ny

# 결과 출력
cleaner(x, y, d)
print(result)