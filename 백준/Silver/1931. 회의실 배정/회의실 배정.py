import sys
input = sys.stdin.readline

N = int(input())  # 회의 개수

time = [[0] * 2 for _ in range(N)]  # 회의 시작/끝 시간
for i in range(N):
    s, e = map(int, input().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key = lambda x: (x[1], x[0]))

cnt = 1  # 최대 회의 개수
end_time = time[0][1]  # 첫번째 회의 끝나는 시간
for i in range(1, N):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)