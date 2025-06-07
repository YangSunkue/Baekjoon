def solution(commands):

    """
    find: 대표를 찾는 함수, 재귀 구현
    union: 병합 함수, merge 구현
    
    50 * 50, (3,4)
    
    2차원 -> 1차원 변환
    0 based
    배열 크기: rows * cols
    1차원 인덱스 변환: r * cols + c
    2차원 인덱스 추적: idx // cols, idx % cols
    
    2500, 154, (3, 4)
    
    1 based
    배열 크기: (rows + 1) * (cols + 1)
    1차원 인덱스 변환: r * (cols+1) + c
    2차원 인덱스 추적: idx // (cols+1), idx % (cols+1)
    
    2601, 157, (3, 4)
    """
    
    """1차원 리스트 사용, 처음엔 자기 자신이 대표"""
    parent = [i for i in range(2601)]
    values = ["" for _ in range(2601)]  # 처음엔 전부 빈 값
    
    """좌표를 1차원 인덱스로 변환하는 함수"""
    def get_idx(r, c):
        return r * 51 + c
    
    """1차원 인덱스를 좌표로 변환하는 함수"""
    def get_coordinate(idx):
        return (idx // 51, idx % 51)
        
    """
    해당 좌표의 대표를 리턴하는 함수
    대표를 찾는 재귀호출 과정에서 거치는, 모든 좌표의 부모를 대표로 바꾼다
    """
    def find(idx):
        if idx != parent[idx]:  # 자기 자신이 대표가 아닐 경우
            parent[idx] = find(parent[idx])
            
        return parent[idx]
    
    """병합 함수"""
    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        
        # 이미 같은 그룹이면 병합하지 않는다
        if x_root == y_root:
            return
        
        if values[y_root] == "":
            parent[y_root] = x_root
        elif values[x_root] == "":
            parent[x_root] = y_root
        else:
            parent[y_root] = x_root
    
    """메인 로직"""
    result = []
    for command in commands:
        cmd = command.split()
        
        if len(cmd) == 4:
            """UPDATE r c value"""
            r, c = map(int, cmd[1:3])
            value = cmd[-1]
            
            # 대표의 값을 변경
            root = find(get_idx(r, c))
            values[root] = value
            
        
        elif len(cmd) == 5:
            """MERGE r1 c1 r2 c2"""
            r1, c1, r2, c2 = map(int, cmd[1:])
            idx1 = get_idx(r1, c1)
            idx2 = get_idx(r2, c2)
            
            # 병합
            union(idx1, idx2)
        
        elif cmd[0] == 'UPDATE':
            """UPDATE value1 value2"""
            value1, value2 = cmd[1], cmd[2]
            
            # 대표의 값만 바꾼다
            for i in range(2601):
                if parent[i] == i and values[i] == value1:
                    values[i] = value2
        
        elif cmd[0] == 'UNMERGE':
            """UNMERGE r c"""
            r, c = map(int, cmd[1:])
            origin_idx = get_idx(r, c)
            root_idx = find(origin_idx)
            saved_value = values[root_idx]
            
            # r,c와 같은 그룹의 모든 셀을 독립적으로 바꾸고 값을 지운다
            unmerge_list = []
            for idx in range(2601):
                if root_idx == find(idx):
                    unmerge_list.append(idx)
            
            for idx in unmerge_list:
                parent[idx] = idx
                values[idx] = ""
            
            # 지정 셀만 기존 값 복원
            values[origin_idx] = saved_value
        
        elif cmd[0] == 'PRINT':
            """PRINT r c"""
            r, c = map(int, cmd[1:])
            root_idx = find(get_idx(r, c))
            
            value = values[root_idx]
            if value == '': value = 'EMPTY'
            
            result.append(value)
    
    return result