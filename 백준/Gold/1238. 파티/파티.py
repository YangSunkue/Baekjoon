from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())  # 노드, 간선, 목적지
adj_list = defaultdict(list)
for _ in range(M):
    s, e, dist = map(int, input().split())
    adj_list[s].append((dist, e))  # 거리, 목적지

to_node = [float('inf')] * (N + 1)  # x에서 각 i번 노드로의 최단거리
to_x = [float('inf')] * (N + 1)  # 각 i번 노드에서 x로의 최단거리

pq = []
heappush(pq, (0, X))

# x에서 각 노드로의 최단거리 구하기
while pq:
    cur_dist, cur_node = heappop(pq)

    if to_node[cur_node] < cur_dist:
        continue

    for dist, next_node in adj_list[cur_node]:
        distance = cur_dist + dist

        if to_node[next_node] > distance:
            to_node[next_node] = distance
            heappush(pq, (distance, next_node))

# 각 노드에서 x로의 최단거리 구하기
for start in range(1, N + 1):

    if start == X:
        continue

    temp_distance = [float('inf')] * (N + 1)
    heappush(pq, (0, start))
    while pq:
        cur_dist, cur_node = heappop(pq)

        if temp_distance[cur_node] < cur_dist:
            continue

        if cur_node == X:
            to_x[start] = cur_dist

        for dist, next_node in adj_list[cur_node]:
            distance = cur_dist + dist

            if temp_distance[next_node] > distance:
                temp_distance[next_node] = distance
                heappush(pq, (distance, next_node))

result = -float('inf')
for i in range(1, N + 1):

    if i == X:
        continue

    total_distance = to_node[i] + to_x[i]
    result = max(result, total_distance)

print(result)