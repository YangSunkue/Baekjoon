import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

G = int(input())
"""
큰 게이트 우선 배정 (수요 적으므로)
parent 이용한 경로 압축
"""
parent = [i for i in range(G + 1)]
visited = set()

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

result = 0
for _ in range(int(input())):

    plane = int(input())  # plane 이하 게이트에만 도킹 가능
    available_gate = find(plane)

    if available_gate in visited:
        break
    
    result += 1
    visited.add(available_gate)

    if available_gate - 1 >= 1:
        parent[available_gate] = available_gate - 1

print(result)