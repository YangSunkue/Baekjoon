import sys
input = sys.stdin.readline

"""
정렬 N log N
투 포인터 N
모든 요소에 대해 투 포인터 N * N

값이 0보다 작으면: left += 1
값이 0보다 크면: right -= 1
"""
N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

diff = float('inf')
result = None
break_flag = False
for a in range(N - 2):

    b = a + 1
    c = N - 1
    while b < c:

        value = liquids[a] + liquids[b] + liquids[c]
        cur_diff = abs(value)

        if cur_diff < diff:
            diff = cur_diff
            result = (liquids[a], liquids[b], liquids[c])

        if value == 0:
            break_flag = True
            break

        elif value < 0:
            b += 1
        else:
            c -= 1

    if break_flag:
        break

print(*result)