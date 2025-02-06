# 실버1 -> 누적 합
"""
N : 표의 크기
M : 합을 구해야 하는 횟수
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(N)]

# dp(누적 합)테이블 생성
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = origin[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

# 메인 로직
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)