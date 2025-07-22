def solution(phone_number):
    
    p = list(phone_number)
    for i in range(len(p) - 5, -1, -1):
        p[i] = '*'
    
    result = ''
    for i in p:
        result += i
        
    return result