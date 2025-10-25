from collections import defaultdict
import heapq

def solution(N, roads, K):
    
    # road를 인접 리스트로 변환
    graph = defaultdict(list)
    for road in roads:
        s, e, w = road[0], road[1], road[2]
        graph[s].append((w, e))  # 가중치, 도착지
        graph[e].append((w, s))  # 양방향으로 초기화
    
    distances = {node: float('inf') for node in range(1, N + 1)}
    distances[1] = 0
    queue = []
    heapq.heappush(queue, (0, 1))  # 가중치, 노드
    
    while queue:
        
        cur_dist, cur_node = heapq.heappop(queue)
        
        if cur_dist > distances[cur_node]:
            continue
            
        for weight, adj_node in graph[cur_node]:
            distance = distances[cur_node] + weight
            
            if distance < distances[adj_node]:
                distances[adj_node] = distance
                heapq.heappush(queue, (distance, adj_node))
    
    result = 0
    for node in distances:
        if distances[node] <= K:
            result += 1
    
    return result