def solution(s):
    
    s = s[2 : len(s) - 2]
    s = s.split('},{')
    s.sort(key=lambda x: len(x))
    
    result = []
    for elem in s:
        for num in elem.split(','):
            num = int(num)
            if num not in result:
                result.append(num)
    
    return result