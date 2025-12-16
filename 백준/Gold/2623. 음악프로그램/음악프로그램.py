from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pds = []
for _ in range(m):
    data = list(map(int, input().split()))
    pds.append(data[1:])

adj_list = defaultdict(list)
in_degree = [0] * (n + 1)
for pd in pds:
    for i in range(len(pd)):
        if i + 1 <= len(pd) - 1:
            adj_list[pd[i]].append(pd[i + 1])
            in_degree[pd[i + 1]] += 1

# 간선이 없는 노드 큐에 넣기
result = []
queue = deque([])
for i in range(1, n + 1):
    if in_degree[i] == 0:
        queue.append(i)
        result.append(i)

while queue:
    cur = queue.popleft()

    for adj_node in adj_list[cur]:
        in_degree[adj_node] -= 1
        if in_degree[adj_node] == 0:
            queue.append(adj_node)
            result.append(adj_node)

if len(result) < n:
    print(0)
else:
    for r in result:
        print(r)