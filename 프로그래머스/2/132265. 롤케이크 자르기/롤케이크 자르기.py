from collections import defaultdict

def solution(topping):

    le = len(topping)

    a_dict = defaultdict(int)
    b_dict = defaultdict(int)

    a_dict[topping[0]] = 1
    for i in range(1, le):
        b_dict[topping[i]] += 1
    
    a_cnt = 1
    b_cnt = len(b_dict)
    if a_cnt == b_cnt:
        result = 1
    else:
        result = 0
    
    for i in range(1, le - 1):

        t = topping[i]

        if a_dict[t] == 0:
            a_cnt += 1
        if b_dict[t] == 1:
            b_cnt -= 1
        
        a_dict[t] += 1
        b_dict[t] -= 1

        if a_cnt == b_cnt:
            result += 1
    
    return result