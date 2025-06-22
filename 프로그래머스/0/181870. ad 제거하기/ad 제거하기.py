def solution(strArr):
    
    for s in strArr[:]:
        if 'ad' in s:
            strArr.remove(s)
            
    return strArr