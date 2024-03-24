import sys

def binarySearch(originList, n, data): # 배열, 배열 길이, 찾을 값
    start = 0
    end = n - 1
    while start <= end:

        mid = (start + end) // 2

        if originList[mid] == data:
            return True
        elif originList[mid] < data:
            start = mid + 1
        else:
            end = mid - 1

    return False

n = int(sys.stdin.readline())
originList = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
goodList = list(map(int, sys.stdin.readline().split()))

originList.sort()
originLen = len(originList)

for i in goodList:
    if binarySearch(originList, originLen, i):
        print('1')
    else:
        print('0')