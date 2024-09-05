import sys
input = sys.stdin.readline

INF = int(1e10)
N, M = map(int, input().split())
number = [int(input()) for _ in range(N)]
number.sort()

def twoPointer():

    result = INF
    start = 0
    end = 1

    while end < N:

        if number[end] - number[start] >= M:
            result = min(result, number[end] - number[start])
            start += 1

            if start == end:
                end += 1
        else:
            end += 1
    
    return result

print(twoPointer())