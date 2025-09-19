def solution(n, k, cmd):

    deleted = []
    up = [i - 1 for i in range(n + 2)]
    down = [i + 1 for i in range(n + 2)]

    k += 1
    for c in cmd:

        if c.startswith('C'):
            up[down[k]] = up[k]
            down[up[k]] = down[k]
            deleted.append(k)

            k = up[k] if n < down[k] else down[k]
        
        elif c.startswith('Z'):
            restore = deleted.pop()
            down[up[restore]] = restore
            up[down[restore]] = restore
        
        else:
            direction, num = c.split(' ')
            
            if direction == 'U':
                for _ in range(int(num)):
                    k = up[k]
            
            elif direction == 'D':
                for _ in range(int(num)):
                    k = down[k]
    
    result = ['O'] * n
    for d in deleted:
        result[d - 1] = 'X'
    
    return ''.join(result)