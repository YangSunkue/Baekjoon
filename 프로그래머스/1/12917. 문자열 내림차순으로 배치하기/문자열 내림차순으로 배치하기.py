def solution(s):
    
    s = list(s)
    s.sort(reverse=True)
    result = ''
    for i in s:
        result += i
    
    return result