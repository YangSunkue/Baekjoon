from collections import defaultdict, deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

adj_list = defaultdict(list)
in_degree = [0] * (n + 1)
for _ in range(m):
    data = list(map(int, input().split()))
    nodes = data[1:]

    for i in range(1, len(nodes)):
        s, e = nodes[i - 1], nodes[i]
        adj_list[s].append(e)
        in_degree[e] += 1

queue = deque([])
result = []
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