from collections import defaultdict, deque
import sys
input = sys.stdin.readline

"""
1. 목표(W)까지 최장거리 구하기
root가 여러개일 수 있음.

다익스트라(최장거리) -> 시간초과
위상 정렬 -> O
"""

for _ in range(int(input())):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))

    adj_list = defaultdict(list)
    indegree = [0] * (N + 1)

    for _ in range(K):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        indegree[e] += 1

    W = int(input())   # 목표 노드

    distances = [0] * (N + 1)
    queue = deque([])

    for i in range(1, N + 1):
        if indegree[i] == 0:
            distances[i] = times[i]
            queue.append(i)
    
    while queue:
        cur = queue.popleft()

        for adj_node in adj_list[cur]:
            distances[adj_node] = max(distances[adj_node], distances[cur] + times[adj_node])

            indegree[adj_node] -= 1
            if indegree[adj_node] == 0:
                queue.append(adj_node)
    
    print(distances[W])