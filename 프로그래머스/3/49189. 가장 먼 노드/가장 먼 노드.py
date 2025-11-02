from heapq import heappush, heappop
from collections import defaultdict

def solution(n, vertex):
    
    adj_list = defaultdict(list)
    for s, e in vertex:
        adj_list[s].append(e)
        adj_list[e].append(s)
    
    distances = [float('inf') for _ in range(n + 1)]
    distances[1] = 0
    
    queue = []
    heappush(queue, (0, 1))  # 거리, 도착노드
    
    while queue:
        cur_dist, cur_node = heappop(queue)
        
        for adj_node in adj_list[cur_node]:
            distance = cur_dist + 1
            
            if distances[adj_node] > distance:
                distances[adj_node] = distance
                heappush(queue, (distance, adj_node))
    
    distances = distances[1:]
    
    max_value = max(distances)
    result = 0
    for d in distances:
        if d == max_value:
            result += 1
    
    return result