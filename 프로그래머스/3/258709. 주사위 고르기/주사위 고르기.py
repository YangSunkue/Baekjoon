from itertools import combinations, product

def binary_search(arr, target):
    
    start = 0
    end = len(arr) - 1
    result = 0
    
    while start <= end:
        
        mid = (start + end) // 2
        
        if arr[mid] < target:
            result = mid + 1
            start = mid + 1
            
        else:
            end = mid - 1
    
    return result

def get_all_sums(dices):
    result = [sum(scores) for scores in product(*dices)]
    return sorted(result)

def solution(dice):
    
    n = len(dice)
    
    a_all_dices_idx = list(combinations(range(n), n // 2))
    max_win_count = -1
    best_combination = None
    
    for a_dices_idx in a_all_dices_idx:
        
        b_dices_idx = [i for i in range(n) if i not in a_dices_idx]
        
        a_dices = [dice[i] for i in a_dices_idx]
        b_dices = [dice[i] for i in b_dices_idx]
        
        a_sums = get_all_sums(a_dices)
        b_sums = get_all_sums(b_dices)
        
        win_count = 0
        for a_sum in a_sums:
            win_count += binary_search(b_sums, a_sum)
        
        if win_count > max_win_count:
            max_win_count = win_count
            best_combination = a_dices_idx
    
    return sorted([i + 1 for i in best_combination])