# 1일차의 최댓값, 2일차의 최댓값, 3일차의 최댓값.. 순으로 N일차의 최댓값까지 구한다
import sys
input = sys.stdin.readline

#  상담 가능 일수
N = int(input())

# 시간과 수익을 따로 입력받는다
time, point = [0 for _ in range(N + 1)], [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    time[i], point[i] = map(int, input().split())

# dp 테이블 만들고, 1일부터 로직 시작
dp = [0 for _ in range(N + 1)]
for i in range(1, N + 1):

    # 기존에 있던 값과 전날 값을 비교해 큰 값으로 설정한다. 기존 값은 finDate에 의해 이미 설정되었을 수 있기 때문
    dp[i] = max(dp[i], dp[i - 1])

    finDate = i + time[i] - 1  # i일 상담이 끝나는 날짜
    if finDate <= N:  # 상담이 가능하다면, 상담 끝나는 날짜에 수익을 추가한다. 단, 기존 값보다 더 클 경우.
        dp[finDate] = max(dp[finDate], dp[i - 1] + point[i])

print(max(dp))