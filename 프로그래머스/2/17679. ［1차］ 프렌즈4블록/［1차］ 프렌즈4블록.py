def solution(m, n, board):
    
    def delete_blocks(m, n, board):
        """
        지울 블록을 찾아 지우는 함수        
        지운 블록 개수를 리턴한다
        """
        # 모든 블록에 대해 2*2 영역이 같은 블록인지 검사 -> 맨아래/우측 제외
        # 검사하면서 지울 블록을 set에 담는다
        deleted_blocks = set()
        
        # 최하단/최우측 제외한 모든 블록을 기준점으로 검사
        for x in range(m - 1):
            for y in range(n - 1):
                
                point = board[x][y]
                if point == '': continue
                block = []
                
                # 각 기준점마다 2*2영역 검사
                for i in range(2):
                    for j in range(2):
                        if board[x+i][y+j] == point:
                            block.append((x+i, y+j))
                
                # 2*2 영역이 전부 같으면 삭제예정 집합에 넣는다
                if len(block) == 4:
                    deleted_blocks.update(block)

        # 블록 지우기
        for x, y in deleted_blocks:
            board[x][y] = ''
            
        return len(deleted_blocks)
    
    def drop_blocks(m, n, board):
        """블록을 떨어뜨리는 함수"""
        
        # 열 단위로 처리
        for y in range(n):
            blocks = []
            
            # 블록 수집
            for x in range(m):
                if board[x][y] != '':
                    blocks.append(board[x][y])
                    board[x][y] = ''
            
            # 수집한 블록을 아래부터 배치
            x_idx = m - 1
            while len(blocks) > 0:
                board[x_idx][y] = blocks.pop()
                x_idx -= 1
                
    """board를 2차원 리스트 형태로 변환"""
    board = [list(row) for row in board]
                
    """메인 로직, 더 이상 블록을 지울 수 없을 때까지 진행"""
    result = 0
    while True:
        
        # 블록 지우기
        count = delete_blocks(m, n, board)
        
        # 더 이상 지울 블록이 없다면 종료
        if count == 0:
            break
        
        # 지운 블록 갱신
        result += count
        
        # 블록 떨어뜨리기
        drop_blocks(m, n, board)
    
    return result