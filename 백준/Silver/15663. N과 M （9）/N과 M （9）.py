import sys
input = sys.stdin.readline

N, M = map(int, input().split())
visited = [False] * N
numbers = list(map(int, input().split()))
numbers.sort()
result = [-1] * M

def backTracking(depth):

    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    temp = 0
    for i in range(N):
        if not visited[i] and temp != numbers[i]:
            result[depth] = numbers[i]
            visited[i] = True
            temp = numbers[i]
            backTracking(depth + 1)
            visited[i] = False

backTracking(0)