def solution(arr):
    
    stk = []
    for i in range(len(arr)):
        if not stk:
            stk.append(arr[i])
        elif stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
    
    return stk if stk else [-1]