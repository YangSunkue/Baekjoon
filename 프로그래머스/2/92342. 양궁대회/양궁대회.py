def solution(n, info):

    def calc_diff_score(info2):
        apeach = 0
        lion = 0

        for i in range(11):
            if (info[i], info2[i]) == (0, 0):
                continue

            if info[i] < info2[i]:
                lion += 10 - i
            else:
                apeach += 10 - i
        return lion - apeach
    
    def select_result(result_list):
        result_list.sort(key = lambda x: x[::-1], reverse=True)
        return result_list[0]
    
    result_list = []
    final_diff = 0
    def back_tracking(score_idx, arrow_used, info2):
        nonlocal final_diff, result_list

        # 10 ~ 1점까지 결정 완료
        if score_idx == 10:
            info2[10] = n - arrow_used
            diff = calc_diff_score(info2)

            if diff > final_diff:
                final_diff = diff
                result_list = [info2[:]]
            elif diff == final_diff:
                result_list.append(info2[:])
            
            # 원상복구
            info2[10] = 0
            return
        
        # 현재 점수 가져가기 (어피치보다 1발 더 필요)
        needed = info[score_idx] + 1
        if (n - arrow_used) >= needed:
            info2[score_idx] = needed
            back_tracking(score_idx + 1, arrow_used + needed, info2)
            info2[score_idx] = 0
        
        # 점수 포기
        back_tracking(score_idx + 1, arrow_used, info2)
    
    back_tracking(0, 0, [0] * 11)
    
    if final_diff < 1:
        return [-1]
    return select_result(result_list)
