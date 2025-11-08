def solution(arr, flag):
    
    result = []
    for i in range(len(arr)):
        if flag[i]:
            for _ in range(arr[i] * 2):
                result.append(arr[i])
        else:
            for _ in range(arr[i]):
                if result: result.pop()
    
    return result