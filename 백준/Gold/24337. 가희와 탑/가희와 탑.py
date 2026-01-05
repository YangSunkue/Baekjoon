from collections import deque
"""
골드 3

"""

N, A, B = map(int, input().split())

result = deque([])
for i in range(1, A):
    result.append(i)
result.append(max(A, B))

for i in range(B - 1, 0, -1):
    result.append(i)

if len(result) > N:
    print(-1)
else:
    temp = result.popleft()
    for _ in range(N - len(result) - 1):
        result.appendleft(1)
        
    result.appendleft(temp)
    print(*result)