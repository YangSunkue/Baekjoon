def solution(n):
    
    watermelon = '수박'
    x = 0
    result = ''
    
    for _ in range(n):
        result += watermelon[x]
        x ^= 1
    
    return result