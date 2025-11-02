def solution(n, times):
    
    left = 0
    right = max(times) * n
    result = 0
    while left <= right:
        
        mid = (left + right) // 2
        
        if sum([mid // time for time in times]) >= n:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result