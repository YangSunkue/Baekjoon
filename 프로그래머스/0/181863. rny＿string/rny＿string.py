def solution(rny_string):
    
    result = ''
    for s in rny_string:
        if s == 'm':
            result += 'rn'
        else:
            result += s
    
    return result