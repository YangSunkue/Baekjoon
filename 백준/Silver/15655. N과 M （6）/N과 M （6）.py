import sys
input = sys.stdin.readline

# 중복 없으며 뒷 숫자가 더 커야 한다

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
box = []

def compare(a, b):
    if a >= b:
        return False
    return True

def backTracking(depth):

    if depth == M:
        print(' '.join(map(str, box)))
        return
    
    for i in range(N):
        if depth == 0 or (numbers[i] not in box and compare(box[depth-1], numbers[i])):
            box.append(numbers[i])
            backTracking(depth + 1)
            box.pop()

backTracking(0)