# DFS
import sys
input = sys.stdin.readline

# 입력받기
N = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(1, N + 1):
    graph[i].append(int(input()))

def DFS(node, start, tmpPath): # 현재노드, 시작노드, 현재경로

    # 방문 체크, 경로 추가
    visited[node] = True
    tmpPath.append(node)

    for nextNode in graph[node]:
        if nextNode in cycle: continue # 이미 싸이클에 포함된 노드일 경우 continue

        if not visited[nextNode]:
            DFS(nextNode, start, tmpPath)

        elif nextNode == start:
            for t in tmpPath:
                cycle.append(t)

# 하나의 노드는 하나의 싸이클에 속한다
# 따라서 이미 싸이클에 들어간 노드는 탐색하지 않음
cycle = []
for start in range(1, N + 1):
    if start not in cycle:
        visited = [False] * (N + 1)
        DFS(start, start, [])

cycle.sort()
print(len(cycle))
for c in cycle:
    print(c)