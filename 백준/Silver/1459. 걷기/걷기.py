"""
실버 3
그리디
"""
import sys
input = sys.stdin.readline

X, Y, W, S = map(int, input().split())

# 직선으로만 갈 때
case1 = (X + Y) * W

# 최대한 대각선으로 가고 남은 거리만 직선으로 갈 때
case2 = (min(X, Y) * S) + (abs(X - Y) * W)

# 대각선으로만 갈 때
if (X + Y) % 2 == 0:
    case3 = max(X, Y) * S
else:
    case3 = (max(X, Y) - 1) * S + W

print(min(case1, case2, case3))