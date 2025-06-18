import sys
input = sys.stdin.readline


def binary_search(child, arr):

    start = 0
    end = len(arr) - 1
    result = len(arr)

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] > child:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return len(arr) - result


P = int(input())
for _ in range(P):

    number, *children = map(int, input().split())

    result = 0
    standing = [children[0]]
    for i in range(1, len(children)):

        count = binary_search(children[i], standing)
        result += count

        idx = len(standing) - count
        standing.insert(idx, children[i])

    print(number, result)