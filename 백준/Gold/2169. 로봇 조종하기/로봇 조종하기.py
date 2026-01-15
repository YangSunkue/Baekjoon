"""
골드 2
DP
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
mars = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
dp[0][0] = mars[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i - 1] + mars[0][i]

left = [[0] * M for _ in range(N)]
right = [[0] * M for _ in range(N)]

# dp 테이블 한 행씩 만들기
for x in range(1, N):
    
    # 위에서 내려온 값 받기
    for y in range(M):
        dp[x][y] = dp[x - 1][y] + mars[x][y]
    
    # 왼쪽에서 온 값
    left[x][0] = dp[x][0]
    for y in range(1, M):
        left[x][y] = max(dp[x][y], left[x][y - 1] + mars[x][y])
    
    # 오른쪽에서 온 값
    right[x][M - 1] = dp[x][M - 1]
    for y in range(M - 2, -1, -1):
        right[x][y] = max(dp[x][y], right[x][y + 1] + mars[x][y])
    
    # 집계 (가장 큰 값 선택)
    for y in range(M):
        dp[x][y] = max(left[x][y], right[x][y])


print(dp[N - 1][M - 1])