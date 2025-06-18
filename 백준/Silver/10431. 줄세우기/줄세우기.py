import sys
input = sys.stdin.readline

"""
자기보다 큰 애들 중 가장 앞에 있는 애 자리에 낀다
모든 학생이 물러난 걸음의 총 합 구하기
"""

P = int(input())

"""
이분 탐색을 통해, 물러날 사람 수를 구한다
"""
def binary_search(child, arr):

    start = 0
    end = len(arr) - 1
    result = len(arr)  # 삽입할 위치

    while start <= end:

        mid = (start + end) // 2

        if arr[mid] > child:
            result = mid
            end = mid - 1

        else:
            start = mid + 1
    
    # 길이 - 삽입할 위치 -> 물러날 사람 수
    return len(arr) - result


for _ in range(P):

    number, *children = map(int, input().split())

    result = 0
    standing = [children[0]]
    for i in range(1, len(children)):

        # 낄 자리 찾기
        count = binary_search(children[i], standing)

        # 물러난 사람 수를 result에 더하기
        result += count

        # 해당 위치에 삽입
        idx = len(standing) - count
        standing.insert(idx, children[i])
    
    print(number, result)