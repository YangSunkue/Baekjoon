from itertools import combinations, product

def binary_search(arr, target):
    """
    이분 탐색
    정렬된 점수 합 리스트를 받아, target보다 작은 요소의 개수를 반환합니다.
    """
    
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
    """
    주사위 리스트를 받아, 정렬된 모든 합 경우의 수 리스트를 리턴합니다.
    순서를 고려하는 product 입니다.
    """
    
    result = [sum(scores) for scores in product(*dices)]
    return sorted(result)

def solution(dice):
    """
    주사위 고르는 경우의 수 구하기 C(n,r) (combination)
    고른 주사위에 대한 점수 합 각각 구하기(6^r + 6^r) (product)
    이분 탐색으로 A가 이기는 횟수 구하기
    -> A의 모든 합을 순회하며, B합 리스트에 대해 이분 탐색
    """
    
    n = len(dice)
    
    # A가 선택한 모든 주사위 인덱스 리스트
    a_all_dices_idx = list(combinations(range(n), n//2))
    
    max_win_count = -1
    result = []
    
    # A가 선택한 모든 주사위 경우의 수에 대해 반복
    for a_dices_idx in a_all_dices_idx:
        
        # B가 선택한 주사위 인덱스
        b_dices_idx = [i for i in range(n) if i not in a_dices_idx]
        
        # 인덱스를 실제 주사위 값으로 변환
        a_dices = [dice[i] for i in a_dices_idx]
        b_dices = [dice[i] for i in b_dices_idx]
        
        # 선택한 주사위로 모든 점수 합 경우의 수 구하기 (각 7776개)
        a_sums = get_all_sums(a_dices)
        b_sums = get_all_sums(b_dices)
        
        # 이분 탐색으로 A의 승리 횟수 구하기
        win_count = 0
        for a_sum in a_sums:
            win_count += binary_search(b_sums, a_sum)
        
        # 승리 횟수 최대값 갱신 및 리턴값 생성
        if win_count > max_win_count:
            max_win_count = win_count
            result = [i + 1 for i in a_dices_idx]
    
    return sorted(result)