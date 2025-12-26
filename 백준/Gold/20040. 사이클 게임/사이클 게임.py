import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = [i for i in range(N)]
rank = [1] * N

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        if rank[x] > rank[y]:
            parent[y] = x
        elif rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            rank[x] += 1

for i in range(1, M + 1):
    s, e = map(int, input().split())

    if find(s) == find(e):
        print(i)
        break

    else:
        union(s, e)
else:
    print(0)