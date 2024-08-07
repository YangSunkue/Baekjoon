import sys
input = sys.stdin.readline

# 1 ~ N 까지의 수, M자리
N, M = map(int, input().split())

def compare(a, b):
    if a > b:
        return False
    return True

def backTracking(depth, num):

    if depth == M:
        print(' '.join(num))
        return
    
    for i in range(1, N + 1):
        if depth == 0 or compare(int(num[-1]), i):
            backTracking(depth + 1, num + str(i))

backTracking(0, '')