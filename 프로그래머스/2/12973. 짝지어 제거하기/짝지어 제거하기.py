def solution(st):

    stack = []

    for s in st:
        if stack:
            item = stack[-1]

            if s == item:
                stack.pop()
                continue
        
        stack.append(s)
    
    if stack:
        return 0
    return 1