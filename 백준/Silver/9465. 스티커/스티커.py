# 실버1(이게?) -> DP
import sys
input = sys.stdin.readline

# 테스트 케이스 개수
T = int(input())

for _ in range(T):
    N = int(input()) # 스티커 길이
    sticker = []
    sticker.append(list(map(int, input().split())))
    sticker.append(list(map(int, input().split())))

    if N == 1:
        print(max(sticker[0][0], sticker[1][0]))
        continue

    dp = [[0] * (N + 1) for _ in range(3)]
    dp[1][1] = sticker[0][0]
    dp[2][1] = sticker[1][0]

    # DP 테이블 채우기
    for i in range(2, N + 1):
        dp[0][i] = max(dp[1][i-1], dp[2][i-1])
        dp[1][i] = max(sticker[0][i-1] + dp[0][i-1], sticker[0][i-1] + dp[2][i-1])
        dp[2][i] = max(sticker[1][i-1] + dp[0][i-1], sticker[1][i-1] + dp[1][i-1])
    
    print(max(dp[1][N], dp[2][N]))