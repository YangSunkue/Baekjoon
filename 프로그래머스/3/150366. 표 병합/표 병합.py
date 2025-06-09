def solution(commands):
    
    def get_idx(r, c):
        return r * 51 + c
    
    def find(idx):
        if parents[idx] != idx:
            parents[idx] = find(parents[idx])
        return parents[idx]
    
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        
        if x_root == y_root:
            return
        
        if values[y_root] == '':
            parents[y_root] = x_root
        elif values[x_root] == '':
            parents[x_root] = y_root
        else:
            parents[y_root] = x_root
    
    
    
    parents = [i for i in range(2601)]
    values = ['' for _ in range(2601)]
    
    result = []
    for command in commands:
        cmd = command.split()
        
        if cmd[0] == 'UPDATE':
            if len(cmd) == 4:
                """UPDATE r c value"""
                r, c = map(int, cmd[1:3])
                value = cmd[-1]
                
                idx = get_idx(r, c)
                root = find(idx)
                
                values[root] = value
            else:
                """UPDATE value1 value2"""
                value1, value2 = cmd[1], cmd[2]
                
                for i in range(2601):
                    if parents[i] == i and values[i] == value1:
                        values[i] = value2
                        
        elif cmd[0] == 'MERGE':
            """MERGE r1 c1 r2 c2"""
            r1, c1, r2, c2 = map(int, cmd[1:])
            
            idx1 = get_idx(r1, c1)
            idx2 = get_idx(r2, c2)
            
            union(idx1, idx2)
            
        elif cmd[0] == 'UNMERGE':
            """UNMERGE r c"""
            r, c = map(int, cmd[1:])
            
            idx = get_idx(r, c)
            root = find(idx)
            saved_value = values[root]
            
            unmerge_targets = []
            for i in range(2601):
                if find(i) == root:
                    unmerge_targets.append(i)
            
            for target in unmerge_targets:
                parents[target] = target
                values[target] = ''
            
            values[idx] = saved_value
            
        elif cmd[0] == 'PRINT':
            """PRINT r c"""
            r, c = map(int, cmd[1:])
            
            idx = get_idx(r, c)
            root = find(idx)
            value = values[root]
            
            if value == '': value = 'EMPTY'
            result.append(value)
    
    return result