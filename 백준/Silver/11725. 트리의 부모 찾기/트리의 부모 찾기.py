# dfs를 구현하고, 방문 리스트와 부모리스트를 사용한다.
# 1번 노드의 인접 노드를 방문할 때, 해당 인접 노드들의 부모는 1이다. 
# 방문 체크만 잘 해주면 부모 노드를 쉽게 구할 수 있다.
import sys
sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]  # 인덱스 번호를 맞추기 위해 + 1
for _ in range(N - 1):
    root, edge = map(int, sys.stdin.readline().split())
    graph[root].append(edge)
    graph[edge].append(root)

visited = [False] * (N + 1)
parent = [[] for _ in range(N + 1)]  # 노드 별 부모 노드를 담을 리스트

def dfs(graph, start, visited):
    visited[start] = True

    for i in graph[start]:
        if visited[i] == False:  # 인접 노드 아직 안갔으면
            parent[i] = start
            dfs(graph, i, visited)

dfs(graph, 1, visited)
for i in range(2, len(parent)):
    print(parent[i])