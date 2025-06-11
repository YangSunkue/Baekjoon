def solution(key, lock):
    
    """
    90도 회전시키는 함수
    자물쇠가 열리는지 확인하는 함수 -> 열쇠를 보드에 적용 + 자물쇠값 모두 1인지 확인 + 열쇠를 보드에서 제거
    
    확장된 보드를 만든다
    자물쇠를 보드 중앙에 배치한다
    열쇠를 4방향으로 회전시키며, 모든 가능한 위치에서 열기 시도한다
    """
    
    """키를 시계 방향으로 90도 회전하는 함수"""
    def rotate_key(key):
        return [list(row) for row in zip(*key[::-1])]
    
    """자물쇠 해제를 시도하는 함수"""
    def try_unlock(x, y, M, N, key, board):
        
        # key를 board에 전부 더하기
        for i in range(M):
            for j in range(M):
                board[x + i][y + j] += key[i][j]
        
        # 모든 자물쇠 값이 1인지 확인
        is_unlocked = True
        for i in range(N):
            for j in range(N):
                if board[M + i][M + j] != 1:
                    is_unlocked = False
                    break
            if is_unlocked == False:
                break
        
        # 자물쇠 원상복구
        for i in range(M):
            for j in range(M):
                board[x + i][y + j] -= key[i][j]
        
        return is_unlocked
    
    """확장된 보드 만들기"""
    M = len(key)
    N = len(lock)
    board_size = M + N + M
    board = [[0] * board_size for _ in range(board_size)]
    
    """자물쇠를 보드 중앙에 배치"""
    for i in range(N):
        for j in range(N):
            board[M + i][M + j] = lock[i][j]
    
    """메인 로직, 모든 위치에 대하여 열기 시도 * 4방향"""
    current_key = key
    for _ in range(4):
        
        for x in range(M + N):
            for y in range(M + N):
                if try_unlock(x, y, M, N, current_key, board):
                    return True
                
        current_key = rotate_key(current_key)
    
    return False