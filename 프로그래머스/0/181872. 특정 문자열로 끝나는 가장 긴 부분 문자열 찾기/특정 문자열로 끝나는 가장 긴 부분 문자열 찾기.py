def solution(my_string, pat):
    
    for i in range(len(my_string), 0, -1):
        if my_string[i - len(pat):i] == pat:
            return my_string[:i]