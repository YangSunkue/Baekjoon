def solution(my_str):
    
    result = []
    temp = ''
    for s in my_str:
        if s in {'a', 'b', 'c'}:
            if 0 < len(temp):
                result.append(temp)
                temp = ''
        else:
            temp += s
    if 0 < len(temp): result.append(temp)
    
    return result if len(result) >= 1 else ['EMPTY']