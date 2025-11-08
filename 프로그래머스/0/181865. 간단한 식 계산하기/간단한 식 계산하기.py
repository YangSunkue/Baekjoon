def solution(binomial):
    
    a, op, b = binomial.split(' ')
    a, b = int(a), int(b)
    
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    else:
        result = a * b
    
    return result