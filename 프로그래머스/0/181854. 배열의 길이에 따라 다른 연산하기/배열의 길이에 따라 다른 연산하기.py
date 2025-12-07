def solution(arr, n):
    
    le = len(arr)
    
    result = []
    if le % 2 == 1:
        for i in range(le):
            if i % 2 == 0:
                result.append(arr[i] + n)
            else:
                result.append(arr[i])
    else:
        for i in range(le):
            if i % 2 == 1:
                result.append(arr[i] + n)
            else:
                result.append(arr[i])
    
    return result