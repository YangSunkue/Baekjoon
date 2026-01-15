"""
골드 2
그리디
"""

import sys
input = sys.stdin.readline

def can_make(matches: int, digits_count: int) -> bool:
    if digits_count == 0:
        return matches == 0
    min_digits = 2 * digits_count
    max_digits = 7 * digits_count
    return min_digits <= matches <= max_digits

cost = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

T = int(input())
for _ in range(T):

    N = int(input())

    digits_goal = (N + 6) // 7
    min_result = ''
    remaining = N


    for d in range(digits_goal):
        start = 1 if d == 0 else 0

        for num in range(start, 10):
            if can_make(remaining - cost[num], digits_goal - d - 1):
                remaining -= cost[num]
                min_result += str(num)
                break
    
    if N % 2 == 1:
        max_result = '7' + '1' * ((N - 3) // 2)
    else:
        max_result = '1' * (N // 2)
    
    print(min_result, max_result)