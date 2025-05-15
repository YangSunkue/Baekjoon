import sys
input = sys.stdin.readline

N = int(input()) # 노드 수
E = int(input()) # 간선 수

graph = [[] for _ in range(N + 1)] # 인접 리스트 - 노드번호와 맞추기 위해 + 1
for _ in range(E):
    node, node2 = map(int, input().split())
    graph[node].append(node2)
    graph[node2].append(node) # 양방향 그래프이므로 양쪽 노드에 추가

visited = [False] * (N + 1)

def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]: # 현재 노드의 인접 노드 차례로 방문
        if visited[i] == False:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(visited.count(True) - 1) # 1번에 의해 감염된 컴퓨터 수 출력