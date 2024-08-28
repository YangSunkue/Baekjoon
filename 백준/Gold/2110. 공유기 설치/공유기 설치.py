import sys
input = sys.stdin.readline

# 집, 공유기 개수
N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]  # 집 좌표
house.sort() # 이분 탐색을 위한 정렬

# 이분 탐색으로 인접 공유기 간의 최소 거리를 찾는다
def binarySearch():

    end = house[-1] - house[0] # 최대 거리
    if C == 2:
        return end

    start = 1 # 최소 거리
    result = 0 # 결과

    # 최적의 거리를 찾을 때까지 반복한다
    while start < end:

        cur = house[0] # 마지막으로 공유기를 설치한 집 ( 첫번째 집에는 반드시 공유기를 설치해야 함 )
        cnt = 1 # 공유기 설치한 개수
        mid = (start + end) // 2

        for i in range(N):
            if house[i] - cur >= mid: # 마지막 설치 위치부터 어떤 집까지의 거리가 최소 거리 이상이라면
                cur = house[i] # 마지막 설치 위치 갱신
                cnt += 1 # 공유기 설치

        if cnt >= C: # 공유기가 충분히 설치되었다면 결과 갱신 및 최소거리 늘려보기
            result = mid
            start = mid + 1
        elif cnt < C: # 공유기가 전부 설치되지 못했다면 최소거리 줄여보기
            end = mid
    
    return result

print(binarySearch())