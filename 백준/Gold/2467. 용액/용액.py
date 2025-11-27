import sys
input = sys.stdin.readline

"""
-3 -2 -1 1 2 3 4
-5 -3 -1 1 2 3

합이 0보다 크면 -> right 줄이기
합이 0보다 작으면 -> left 올리기
"""

N = int(input())
liquid = list(map(int, input().split()))

diff = int(1e10)
result = None

left = 0
right = N - 1
while left < right:

    value = liquid[left] + liquid[right]
    cur_diff = abs(value)

    if cur_diff < diff:
            diff = cur_diff
            result = (liquid[left], liquid[right])

    if value == 0:
        break

    if value > 0:
        right -= 1
    else:
         left += 1

print(*result)