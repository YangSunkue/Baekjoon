def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    
    current_min = int(1e9)
    idx = -1
    for i, item in enumerate(arr):
        if item < current_min:
            current_min = item
            idx = i
            
    del arr[idx]
    return arr