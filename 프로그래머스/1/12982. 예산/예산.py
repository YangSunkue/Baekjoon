def solution(d_list, budget):
    
    d_list.sort()
    
    result = 0
    for d in d_list:
        if d <= budget:
            budget -= d
            result += 1
    
    return result