from collections import defaultdict, deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

"""
양방향 그래프
"""

N, R, Q = map(int, input().split())

adj_list = defaultdict(list)
for _ in range(N - 1):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

parents = [-1] * (N + 1)

visited = [False] * (N + 1)
visited[R] = True
queue = deque([R])
while queue:

    cur = queue.popleft()

    for node in adj_list[cur]:
        if not visited[node]:
            parents[node] = cur
            visited[node] = True

            queue.append(node)

dp = [0] * (N + 1)

def dfs(cur):
    size = 1

    for node in adj_list[cur]:
        if parents[cur] == node:
            continue
        size += dfs(node)
    
    dp[cur] = size
    return size


dfs(R)
for _ in range(Q):
    root = int(input())
    print(dp[root])