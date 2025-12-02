def solution(arr):
    
    two = [1]
    for i in range(1, 11):
        two.append(2**i)
    
    for i in range(11):
        if len(arr) == two[i]:
            return arr
        
        if len(arr) < two[i]:
            return arr + ([0] * (two[i] - len(arr)))