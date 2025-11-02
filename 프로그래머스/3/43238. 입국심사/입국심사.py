def solution(n, times):
    
    """
        시간 기준 이분탐색
    
        -> 특정 시간에 대해서, 몇 명의 사람을 심사할 수 있는가?
    """
    
    def calculate_people(time):
        return sum([time // t for t in times])
    
    start = 0
    end = max(times) * n
    result = 0
    while start <= end:
        
        mid = (start + end) // 2
        
        if calculate_people(mid) >= n:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    
    return result