import heapq

graph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'C': 8, 'D': 9, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 15, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 15, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}
}

distance = 0

def prim(graph):
    global distance
    mst = []
    visited = set()  # 트리에 포함된 정점을 저장할 집합

    start_node = list(graph.keys())[0]  # 그래프의 첫번째 정점 선택 -> 'A'
    visited.add(start_node) # -> 'A' 를 넣는다

    edges = [(cost, start_node, end_node) for end_node, cost in graph[start_node].items()] # startNode에 대한 연결정보를 edges에 저장
    heapq.heapify(edges)  # edges를 우선순위큐로 만든다

    while edges:
        cost, start, end = heapq.heappop(edges)

        if end not in visited:  # 도착지가 아직 트리에 포함안됐으면
            visited.add(end)  # 방문체크하고 포함시킨다
            mst.append((start, end, cost))
            distance += cost

            for next_end, next_cost in graph[end].items(): # 다음도착지의 연결정보에 대하여 반복
                if next_end not in visited:  # 안갔으면 큐에 추가
                    heapq.heappush(edges, (next_cost, end, next_end))

    return mst

print(prim(graph))
print(distance)