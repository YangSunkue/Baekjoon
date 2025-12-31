from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())  # 노드, 간선, 목적지
adj_list = defaultdict(list)
rvs_list = defaultdict(list)
for _ in range(M):
    s, e, dist = map(int, input().split())
    adj_list[s].append((dist, e))  # 거리, 목적지
    rvs_list[e].append((dist, s))

"""
X 시작 기준
기본 그래프 다익스트라: X -> 각 노드 최단거리
역방향 그래프 다익스트라: 각 노드 -> X 최단거리
"""

def dijkstra(start, graph) -> list[int]:

    distances = [float('inf')] * (N + 1)
    pq = []
    heappush(pq, (0, start))

    while pq:
        cur_dist, cur_node = heappop(pq)

        if cur_dist > distances[cur_node]:
            continue

        for dist, next_node in graph[cur_node]:
            distance = cur_dist + dist

            if distance < distances[next_node]:
                distances[next_node] = distance
                heappush(pq, (distance, next_node))
    
    return distances

to_x = dijkstra(X, adj_list)
to_node = dijkstra(X, rvs_list)
total_distances = [to_x[i] + to_node[i] for i in range(1, N + 1) if i != X]
print(max(total_distances))