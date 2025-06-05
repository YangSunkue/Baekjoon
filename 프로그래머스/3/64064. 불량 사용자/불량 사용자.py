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
            result_set.add(frozenset(selected))
            return
        
        for user in user_id:
            if user not in selected and is_match(user, banned_id[depth]):
                selected.add(user)
                back_tracking(depth + 1, selected)
                selected.remove(user)
    
    result_set = set()
    back_tracking(0, set())
    
    return len(result_set)