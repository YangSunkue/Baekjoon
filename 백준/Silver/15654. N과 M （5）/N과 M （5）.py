import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))
numList.sort()
box = []

def backTracking(depth):

    if depth == M:
        print(' '.join(map(str, box)))
        return
    
    for i in range(N):
        if not numList[i] in box:

            box.append(numList[i])
            backTracking(depth + 1)
            box.pop()

backTracking(0)