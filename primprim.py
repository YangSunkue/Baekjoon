import heapq
import sys

input = sys.stdin.readline

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())  # 출발, 도착, 비용
    graph[a].append((c, b))
    graph[b].append((c, a))

visited = [False] * (N + 1)
distance = 0
def prim(graph, start):  # 그래프, 시작노드 입력받기
    global distance

    mst = []
    visited[start] = True

    edges = [(cost, start, end) for cost, end in graph[start]]  # 연결목록 미리 만들어서 리스트화 + heapq변환
    heapq.heapify(edges)

    while edges:
        cost, start, end = heapq.heappop(edges)

        if visited[end] == False:
            visited[end] = True
            mst.append((start, end, cost))
            distance += cost

            for nextCost, nextEnd in graph[end]:
                if visited[nextEnd] == False:
                    heapq.heappush(edges, (nextCost, end, nextEnd))
    
    return mst

prim(graph, 1)
print(distance)



# 7 11
# 1 2 7
# 1 4 5
# 2 3 8
# 2 4 9
# 2 5 7
# 3 5 5
# 4 5 15
# 4 6 6
# 5 6 8
# 5 7 9
# 6 7 11
