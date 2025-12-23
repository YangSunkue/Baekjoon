import sys
input = sys.stdin.readline

N = int(input())
sequence = [0] + list(map(int, input().split()))

"""dp 테이블 제작"""
dp = [[0] * (N + 1) for _ in range(N + 1)]  # dp[i][j]: i번째부터 j번째까지가 팰린드롬인지 여부

# 길이 1은 전부 팰린드롬
for i in range(1, N + 1):
    dp[i][i] = 1

# 길이 2는 두 수가 같을 경우 팰린드롬
for i in range(1, N):
    if sequence[i] == sequence[i + 1]:
        dp[i][i + 1] = 1

# 짧은 길이부터 반복문 돌리기 (3 ~ N)
for size in range(3, N + 1):
    for i in range(1, N - (size - 2)):
        j = i + (size - 1)

        if sequence[i] == sequence[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

"""정답 출력"""
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s][e])