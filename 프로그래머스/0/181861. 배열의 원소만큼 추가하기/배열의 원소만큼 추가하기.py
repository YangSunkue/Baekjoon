def solution(arr):
    
    result = []
    for num in arr:
        for _ in range(num):
            result.append(num)
            
    return result