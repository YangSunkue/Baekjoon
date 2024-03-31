from collections import deque
import sys

input = sys.stdin.readline
N, E = map(int, input().split())
indegree = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    root, edge = map(int, input().split())
    graph[root].append(edge)
    indegree[edge] += 1

def solve():
    queue = deque()
    result = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
    
    while queue:
        here = queue.popleft()
        result.append(here)

        for i in graph[here]:
            indegree[i] -= 1
            if indegree[i] == 0:
                queue.append(i)
    
    return result

result = solve()
for re in result:
    print(re, end=' ')