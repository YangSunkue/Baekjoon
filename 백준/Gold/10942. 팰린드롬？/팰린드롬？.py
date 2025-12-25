import sys
input = sys.stdin.readline

N = int(input())
sequence = [0] + list(map(int, input().split()))

"""dp 테이블 제작"""
dp = [[0] * (N + 1) for _ in range(N + 1)]

# 길이 1 -> 전부 팰린드롬
for i in range(1, N + 1):
    dp[i][i] = 1

# 길이 2 -> 두 수가 같으면 팰린드롬
for i in range(1, N):
    if sequence[i] == sequence[i + 1]:
        dp[i][i + 1] = 1

# 길이 3 이상 -> sequence[i], [j]가 같고 [i + 1][j - 1]이 팰린드롬이면 팰린드롬
for size in range(3, N + 1):
    for i in range(1, N - (size - 2)):
        j = i + (size - 1)

        if sequence[i] == sequence[j] and dp[i + 1][j - 1] == 1:
            dp[i][j] = 1

"""정답 출력"""
for _ in range(int(input())):
    s, e = map(int, input().split())
    print(dp[s][e])