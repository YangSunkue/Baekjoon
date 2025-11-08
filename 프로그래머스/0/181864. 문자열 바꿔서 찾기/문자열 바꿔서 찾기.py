def solution(my_string, pat):
    
    string = ''
    for s in my_string:
        if s == 'A':
            string += 'B'
        else:
            string += 'A'
    
    return 1 if pat in string else 0