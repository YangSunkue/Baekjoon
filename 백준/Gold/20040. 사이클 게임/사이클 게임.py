import sys
input = sys.stdin.readline

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]

"""
무방향 그래프 만들어 가면서 싸이클 찾기

간선 추가할 때마다 Union-find로 싸이클 확인
"""

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):

    x_root = find(x)
    y_root = find(y)

    if x_root != y_root:
        if rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        elif rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

parent = [i for i in range(N)]
rank = [1] * N

for i, (s, e) in enumerate(edges):

    if find(s) == find(e):
        print(i + 1)
        break

    union(s, e)
else:
    print(0)