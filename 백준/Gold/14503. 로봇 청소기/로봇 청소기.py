# 구현, 시뮬레이션
import sys
input = sys.stdin.readline

# 입력받기
N, M = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

# 사전준비
directions = [3, 2, 1, 0]  # 서, 남, 동, 북
num = directions.index(d)   # directions[num % 4] 하면 방향 나옴
dx = [0, 1, 0, -1]          # 서, 남, 동, 북
dy = [-1, 0, 1, 0]

result = 0  # 시작 위치도 청소하므로 0으로 초기화
def cleaner(x, y, num):
    global result

    # 시작 위치 청소
    room[x][y] = 2
    result += 1

    for _ in range(50 * 50 * 50):  # 무한 루프 방지
        found_cleanable = False  # 미청소 칸을 찾았는지 여부

        # 미청소 칸 탐색
        for _ in range(4):
            # 반시계 방향으로 회전
            num = (num + 1) % 4
            nx = x + dx[num]
            ny = y + dy[num]

            # 다음 경로가 미청소 빈칸이면 결과 및 좌표 갱신
            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                room[nx][ny] = 2  # 청소
                result += 1
                x, y = nx, ny
                found_cleanable = True
                break
        
        # 4방향 모두 갈 곳이 없을 경우 후진 (진행 방향의 반대)
        if not found_cleanable:
            nx = x + dx[(num + 2) % 4]
            ny = y + dy[(num + 2) % 4]

            # 후진시 벽일 경우 종료
            if room[nx][ny] == 1:  # 벽이면 종료
                return
            x, y = nx, ny  # 후진

# 결과 출력
cleaner(x, y, num)
print(result)
