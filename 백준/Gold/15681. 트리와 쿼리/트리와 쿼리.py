from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

"""
양방향 그래프
"""

N, R, Q = map(int, input().split())

adj_list = defaultdict(list)
for _ in range(N - 1):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

dp = [0] * (N + 1)

def dfs(cur, parent):
    size = 1

    for node in adj_list[cur]:
        if node == parent:
            continue
        size += dfs(node, cur)
    
    dp[cur] = size
    return size

dfs(R, -1)
for _ in range(Q):
    root = int(input())
    print(dp[root])