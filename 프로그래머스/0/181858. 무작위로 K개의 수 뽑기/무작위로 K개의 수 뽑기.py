def solution(arr, k):
    
    visited = set()
    result = []
    
    for num in arr:
        if num not in visited:
            visited.add(num)
            result.append(num)
        
        if len(result) == k:
            return result
    
    result += [-1] * (k - len(result))
    return result