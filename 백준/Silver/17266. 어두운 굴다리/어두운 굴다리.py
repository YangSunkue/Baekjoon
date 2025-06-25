import sys
input = sys.stdin.readline

"""
N: 0~N 굴다리 길이
M: 가로등 개수
lamps: 각 가로등의 위치 (x)
-> 각 가로등은 높이만큼 주위 양 옆을 비춘다. 높이는 모두 같다
-> 가로등 개수, 위치는 정해져 있고, 모든 길을 비추는 최소 높이를 구하자

높이를 구한 후, 모든 길을 비추는 지를 어떻게 확인?
-> 그건 그냥 대충 구하고 경우의수를 이분탐색으로 줄이면될듯.
"""

"""특정 높이를 가진 가로등이 모든 길을 비출 수 있는지 판단한다"""
def is_valid(N, height, lamps):

    # 각 가로등은 x - height 부터 x + (height - 1)까지 비춘다.
    prev = 0  # 비추기 시작해야 하는 지점
    for x in lamps:

        # 가로등이 이전 불빛에 이어서 비추고 있으면 prev 갱신
        if x - height <= prev:
            prev = x + height
        
        # 빈 곳이 있으면 False
        else:
            return False

        # 모든 길을 밝혔다면 True 리턴
        if prev >= N:
            return True
    
    return False

N = int(input())
M = int(input())
lamps = list(map(int, input().split()))

"""이분 탐색으로 최소 높이를 찾는다"""
start = 0
end = N
min_height = end
while start <= end:

    mid = (start + end) // 2

    # 다 비출 수 있으면 높이 줄이기
    if is_valid(N, mid, lamps):
        min_height = mid
        end = mid - 1
    
    # 다 비출 수 없으면 높이 늘리기
    else:
        start = mid + 1

print(min_height)