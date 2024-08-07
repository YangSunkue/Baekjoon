import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False] * N
result = [-1] * M

def backTracking(depth):

    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    temp = 0
    for i in range(N):
        if not visited[i] and temp != numbers[i]:
            result[depth] = numbers[i]
            temp = numbers[i]
            visited[i] = True
            backTracking(depth + 1)
            visited[i] = False

backTracking(0)