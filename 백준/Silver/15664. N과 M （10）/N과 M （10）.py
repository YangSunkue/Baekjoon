import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = [False] * N
result = [-1] * M

def compare(a, b):
    if a > b:
        return False
    return True

def backTracking(depth):

    if depth == M:
        print(' '.join(map(str, result)))
        return
    
    temp = 0
    for i in range(N):
        if (depth == 0 and temp != numbers[i]) or (not visited[i] and temp != numbers[i] and compare(result[depth - 1], numbers[i])):
            visited[i] = True
            temp = numbers[i]
            result[depth] = numbers[i]
            backTracking(depth + 1)
            visited[i] = False
    
backTracking(0)