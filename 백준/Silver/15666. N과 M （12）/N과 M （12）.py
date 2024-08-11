import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
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
        if temp != numbers[i] and (depth == 0 or compare(result[depth-1], numbers[i])):
            temp = numbers[i]
            result[depth] = numbers[i]
            backTracking(depth + 1)
    
backTracking(0)