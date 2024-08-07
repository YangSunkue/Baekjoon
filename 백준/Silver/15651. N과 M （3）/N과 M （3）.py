import sys
input = sys.stdin.readline

# 1 ~ N 까지의 수 / 길이는 M
N, M = map(int, input().split())
result = []

def backTracking(depth, num):
    
    if depth == M:
        result.append(' '.join(num))
        return
    
    for i in range(1, N + 1):
        backTracking(depth + 1, num + str(i))

backTracking(0, '')
for re in result:
    print(re)