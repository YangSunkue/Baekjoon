import sys
input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split())) + [0]

stack = []
result = [-1] * N
for i in range(len(sequence)):
    while stack and sequence[i] > sequence[stack[-1]]:
        result[stack.pop()] = sequence[i]

    stack.append(i)

print(*result)