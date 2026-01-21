"""
실버 1
그리디
"""
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort()

    min_interview = data[0][1]

    result = 0
    for _, interview in data:
        if interview <= min_interview:
            result += 1
            min_interview = interview
    
    print(result)