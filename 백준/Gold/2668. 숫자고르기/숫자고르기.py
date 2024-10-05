# DFS
import sys
input = sys.stdin.readline

# 입력받기
N = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i].append(int(input())) # 역방향 그래프

def DFS(node, start):

    visited[node] = True

    for nextNode in graph[node]:
        if nextNode == start: # 사이클 발견
            cycle.add(start)
            return # 한 노드당 사이클은 하나뿐이다
        
        if not visited[nextNode]:
            DFS(nextNode, start)

cycle = set()
for start in range(1, N + 1):
    if start not in cycle:
        visited = [False] * (N + 1)
        DFS(start, start)

result = sorted(list(cycle))
print(len(result))
for re in result:
    print(re)