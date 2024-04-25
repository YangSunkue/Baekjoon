import sys
input = sys.stdin.readline

N = int(input())

# time, point 따로 입력받기
time, point = [0 for _ in range(N + 1)], [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    time[i], point[i] = map(int, input().split())

# dp 테이블 만들기
dp = [0 for _ in range(N + 1)]

# 첫째 날(1)부터 로직 시작
for i in range(1, N + 1):
    print(dp)
    # 오늘과 전날 중 큰 값으로 설정, 아래 dp[i]는 findate에 의해서 미리 등록되었을 수 있으니까
    dp[i] = max(dp[i], dp[i - 1])


    fin_date = i + time[i] - 1  # i일 상담이 끝나는 날
    # 상담이 N일 내에 끝나면 상담 끝나는 날 값을 설정한다
    # 기존 값 vs 전날 + 상담포인트
    if fin_date <= N:
        dp[fin_date] = max(dp[fin_date], dp[i - 1] + point[i])


print(max(dp))