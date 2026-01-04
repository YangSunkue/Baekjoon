"""
골드 3
스택

오른쪽으로 한번, 왼쪽으로 한번 순회
"""
import sys
input = sys.stdin.readline

N = int(input())
b = [0] + list(map(int, input().split()))

left = [[0] * 2 for _ in range(N + 1)]
right = [[0] * 2 for _ in range(N + 1)]

stack = []
for idx in range(1, N + 1):
    while stack and b[stack[-1]] <= b[idx]:
        stack.pop()
    
    if stack:
        left[idx][0] = len(stack)
        left[idx][1] = stack[-1]
    
    stack.append(idx)

stack = []
for idx in range(N, 0, -1):
    while stack and b[stack[-1]] <= b[idx]:
        stack.pop()
    
    if stack:
        right[idx][0] = len(stack)
        right[idx][1] = stack[-1]

    stack.append(idx)

result = [[0] * 2 for _ in range(N + 1)]
for i in range(1, N + 1):

    result[i][0] = left[i][0] + right[i][0]

    l, r = left[i][1], right[i][1]
    l_dist, r_dist = abs(i - l), abs(i - r)

    if l == 0 and r == 0:
        result[i][1] = 0
    elif l > 0 and r > 0:
        if l_dist < r_dist:
            result[i][1] = l
        elif l_dist > r_dist:
            result[i][1] = r
        else:
            result[i][1] = min(l, r)
    elif l == 0 or r == 0:
        result[i][1] = max(l, r)

for r in result[1:]:
    print(0) if r[0] == 0 else print(*r)