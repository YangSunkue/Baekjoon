import math

def solution(n, stations, w):
    
    """
    기지국 위치를 이용해 각 빈 곳들의 크기를 구하기
    빈 곳에 최대한 적게 세우기
    """
    
    result = 0
    
    # 앞, 뒤 기지국 구하기
    front = stations[0] - w - 1
    back = n - (stations[-1] + w)
    if front > 0:
        result += math.ceil(front / ((w * 2) + 1))
    if back > 0:
        result += math.ceil(back / ((w * 2) + 1))
    
    # 사이사이 기지국 구하기
    for i in range(1, len(stations)):
        
        right = stations[i]
        left = stations[i - 1]
        
        r_range = right - w
        l_range = left + w
        
        empty = r_range - l_range - 1
        
        if empty > 0:
            result += math.ceil(empty / ((w * 2) + 1))
        
    return result