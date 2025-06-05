def solution(user_id, banned_id):
    
    def is_match(user, banned_user):
        if len(user) != len(banned_user):
            return False
        
        for i in range(len(user)):
            if banned_user[i] != '*' and banned_user[i] != user[i]:
                return False
        return True
    
    def back_tracking(depth, selected):
        
        if depth == len(banned_id):
            result_set.add(frozenset(selected))  # 순서가 다른것도 중복으로 인식하도록 frozenset 사용
            return
        
        for user in user_id:
            if user not in selected and is_match(user, banned_id[depth]):
                selected.add(user)
                back_tracking(depth + 1, selected)
                selected.remove(user)
            
            
            
    # set으로 바꿔 중복 제거 (순서만 다른 조합들)
    result_set = set()
    back_tracking(0, set()) # not in 연산 효율성을 위해 set 선택(key로 접근하는 O(1)), 리스트는 O(N)
    
    return len(result_set)