"""
골드 1

1번째 ~ M번째 신호 까지 존재
1분 동안 초록불 들어옴, 나머지 빨간불

1분마다 계속 바뀜

"""
from heapq import heappush, heappop
from collections import defaultdict
import sys
input = sys.stdin.readline

def calc_wait(cur_time, edge) -> int:
    """cur_time 시간에서 edge번 횡단보도를 건너기 위해 대기해야 하는 시간"""
    t = cur_time % M
    if t <= edge:
        return abs(t - edge)
    else:
        return M - (t - edge)

N, M = map(int, input().split())  # 지역 수, 주기
adj_list = defaultdict(list)
for i in range(M):
    s, e = map(int, input().split())
    s, e = s - 1, e - 1
    adj_list[s].append((i, e))  # (번호, 도착노드)
    adj_list[e].append((i, s))

distances = [float('inf')] * N
distances[0] = 0
pq = []
heappush(pq, (0, 0))  # 현재까지 시간, 현재노드
while pq:

    cur_time, cur_node = heappop(pq)
    if cur_node == N - 1:
        break

    if distances[cur_node] < cur_time:
        continue

    for edge, adj_node in adj_list[cur_node]:
        wait_time = calc_wait(cur_time, edge)
        distance = cur_time + wait_time + 1

        if distance > distances[adj_node]:
            continue
        
        distances[adj_node] = distance
        heappush(pq, (distance, adj_node))

print(distances[N - 1])