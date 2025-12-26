from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

adj_list = defaultdict(list)
in_degree = [0] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    in_degree[e] += 1

pq = []
for i in range(1, N + 1):
    if in_degree[i] == 0:
        heappush(pq, i)  # 간선이 없는 가장 작은 노드부터 나오게 처리

result = []
while pq:
    cur_node = heappop(pq)
    result.append(cur_node)

    for adj_node in adj_list[cur_node]:
        in_degree[adj_node] -= 1

        if in_degree[adj_node] == 0:
            heappush(pq, adj_node)

print(*result)