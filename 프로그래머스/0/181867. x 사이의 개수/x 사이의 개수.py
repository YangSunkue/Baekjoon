def solution(my_string):
    
    cnt = 0
    result = []
    for s in my_string:
        if s != 'x':
            cnt += 1
        else:
            result.append(cnt)
            cnt = 0
    result.append(cnt)
    
    return result