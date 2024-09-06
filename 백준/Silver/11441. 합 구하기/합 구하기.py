import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
M = int(input())

result = [0 for _ in range(N + 1)] # 입력값과 인덱스를 맞추기 위해 + 1
result[1] = numbers[0]
for i in range(2, N + 1):
    result[i] = result[i-1] + numbers[i-1]

for _ in range(M):

    i, j = map(int, input().split())

    if i == 1:
        print(result[j])
    else:
        print(result[j] - result[i-1])