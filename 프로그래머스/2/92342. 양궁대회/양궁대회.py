def solution(n, info):
    
    def select_result(result_list):
        result_list.sort(key=lambda x: x[::-1], reverse=True)
        return result_list[0]
    
    def calculate_diff(info2):
        lion = 0
        apeach = 0
        
        for i in range(11):
            if (info[i], info2[i]) == (0, 0):
                continue
            
            if info2[i] > info[i]:
                lion += 10 - i
            else:
                apeach += 10 - i
        
        return lion - apeach
        
    
    result_list = []
    final_diff = 0
    def back_tracking(arrow_idx, used_arrow, info2):
        
        nonlocal result_list, final_diff
        
        if arrow_idx == 10:
            info2[arrow_idx] = n - used_arrow
            
            diff = calculate_diff(info2)
            if final_diff < diff:
                final_diff = diff
                result_list = [info2[:]]
            elif final_diff == diff:
                result_list.append(info2[:])
            
            info2[arrow_idx] = 0
            return
        
        needed = info[arrow_idx] + 1
        if (n - used_arrow) >= needed:
            info2[arrow_idx] = needed
            back_tracking(arrow_idx + 1, used_arrow + needed, info2)
            info2[arrow_idx] = 0
        
        back_tracking(arrow_idx + 1, used_arrow, info2)
    
    back_tracking(0, 0, [0] * 11)
    
    if final_diff < 1:
        return [-1]
    return select_result(result_list)