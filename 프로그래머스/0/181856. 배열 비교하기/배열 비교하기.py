def solution(arr1, arr2):
    
    l1 = len(arr1)
    l2 = len(arr2)
    
    if l1 > l2:
        return 1
    elif l1 < l2:
        return -1
    else:
        l1 = sum(arr1)
        l2 = sum(arr2)
        
        if l1 > l2:
            return 1
        elif l1 < l2:
            return -1
        else:
            return 0