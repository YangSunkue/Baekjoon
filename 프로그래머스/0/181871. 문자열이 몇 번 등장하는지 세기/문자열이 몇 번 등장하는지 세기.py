def solution(myString, pat):
    
    left = 0
    right = left + len(pat)
    result = 0
    while right <= len(myString):
        if myString[left:right] == pat:
            result += 1
            
        left += 1
        right += 1
    
    return result