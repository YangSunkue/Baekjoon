import sys
sys.setrecursionlimit(10 ** 9)

N = int(sys.stdin.readline())  # 노드의 개수
graph = [[] for _ in range(N + 1)]  # 노드번호와 인덱스번호 동기화를 위해 N + 1
for _ in range(N - 1):  # 연결정보 입력받기
    root, edge = map(int, sys.stdin.readline().split())
    graph[root].append(edge)
    graph[edge].append(root)

visited = [False] * (N + 1)
parent = [[] for _ in range(N + 1)]  # 노드번호와 인덱스번호 동기화를 위해 N + 1

def dfs(graph, v, visited):
    visited[v] = True  # 왔으니 방문체크

    for i in graph[v]:
        if visited[i] == False:  # 아직 방문 안한 인접 노드로 간다
            parent[i] = v  # 부모 노드값 입력
            dfs(graph, i, visited)

dfs(graph, 1, visited)
for i in range(2, len(parent)):
    print(parent[i])