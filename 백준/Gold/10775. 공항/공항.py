import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

G = int(input())

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

parent = [i for i in range(G + 1)]
result = 0
for _ in range(int(input())):

    plane = int(input())
    available_gate = find(plane)

    if available_gate == 0:
        break

    parent[available_gate] -= 1
    result += 1

print(result)