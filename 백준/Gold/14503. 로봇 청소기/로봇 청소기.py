# 구현, 시뮬레이션
import sys
input = sys.stdin.readline

# 입력받기
N, M = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]


# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

room[x][y] = 2
result = 1
def cleaner(x, y, d):

    global result

    for _ in range(50**3): # 혹시 모를 무한루프 방지

        clean = False # 청소했는지 여부

        # 미청소 칸 탐색
        for _ in range(4):
            # 반시계 회전 후 다음 경로 지정
            d = (d + 3) % 4
            nx = x + dx[d]
            ny = y + dy[d]

            # 다음 경로가 미청소 빈칸이면 결과 및 좌표 갱신
            if room[nx][ny] == 0:
                clean = True
                room[nx][ny] = 2
                result += 1
                x, y = nx, ny
                break
        
        # 4방향 모두 갈 곳이 없을 경우 후진 ( 진행방향의 반대 )
        # 순환적으로 인덱스 2 증가시키면 반대 방향임
        if not clean:
            tmp = (d + 2) % 4
            nx = x + dx[tmp]
            ny = y + dy[tmp]

            # 후진시 벽일 경우 종료
            if room[nx][ny] == 1:
                return
            x, y = nx, ny

# 결과 출력
cleaner(x, y, d)
print(result)