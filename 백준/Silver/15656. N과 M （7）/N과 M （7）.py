import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
box = []

def backTracking(depth):

    if depth == M:
        print(' '.join(map(str, box)))
        return
    
    for i in range(N):
        box.append(numbers[i])
        backTracking(depth + 1)
        box.pop()

backTracking(0)