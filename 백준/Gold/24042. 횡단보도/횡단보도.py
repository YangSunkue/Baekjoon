"""
골드 1
다익스트라 (가중치가 변하는 다익스트라)

0 based로 통일
"""
from collections import defaultdict
from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def get_wait(cur_time, edge) -> int:
    t = cur_time % M
    if t <= edge:
        return abs(t - edge)
    else:
        return M - (t - edge)

N, M = map(int, input().split())
adj_list = defaultdict(list)
for i in range(M):
    s, e = map(int, input().split())
    s, e = s - 1, e - 1

    adj_list[s].append((i, e))
    adj_list[e].append((i, s))

distances = [float('inf')] * N
distances[0] = 0

pq = []
heappush(pq, (0, 0))  # (현재까지 거리, 현재노드)
while pq:

    cur_time, cur_node = heappop(pq)

    if cur_node == N - 1:
        break

    if distances[cur_node] < cur_time:
        continue

    for edge, adj_node in adj_list[cur_node]:
        distance = cur_time + get_wait(cur_time, edge) + 1

        if distance > distances[adj_node]:
            continue

        distances[adj_node] = distance
        heappush(pq, (distance, adj_node))

print(distances[N - 1])