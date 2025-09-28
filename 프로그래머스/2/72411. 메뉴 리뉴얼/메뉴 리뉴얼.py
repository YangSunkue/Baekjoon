from collections import defaultdict

def solution(orders, course):
    
    """
    모든 orders에 대해, course길이의 모든 조합 구하기
    각 조합을 딕셔너리 key로 해서 주문횟수 세기
    주문횟수로 내림차순 정렬하고, 0번부터 결과 찾아서 result에 저장
    """
    
    # 입력된 문자열과 목표 길이에 맞는 조합을 구하는 함수
    def get_combination(string, cur_string, goal_depth, cur_depth, pointer):

        if cur_depth == goal_depth:
            orders_dict[cur_string] += 1
            return
        
        for i in range(pointer, len(string)):
            cur_string += string[i]
            get_combination(string, cur_string, goal_depth, cur_depth + 1, i + 1)
            cur_string = cur_string[:-1]
    
    # 주문 알파벳순 정렬하기 (순서 바뀐 같은 조합 방지)
    for i in range(len(orders)):
        orders[i] = sorted(list(orders[i]))

    # 조합 길이별로 나눠 결과 구하기
    result = []
    for c in course:

        orders_dict = defaultdict(int)  # {'AB': 2, 'AC': 3 ...}

        # c 길이 모든 각 조합의 개수 구하기 (orders_dict에 저장)
        for order in orders:
            get_combination(order, '', c, 0, 0)

        if len(orders_dict) == 0:
            continue

        # 많이 사용된 순서대로 정렬
        sorted_orders = sorted(orders_dict.items(), key=lambda x: -x[1])

        # 두 번 이상 주문된 조합이 없다면
        max_order = sorted_orders[0][1]
        if max_order < 2:
            continue
        
        # 가장 많이 주문된 조합 전부 결과에 추가
        for order in sorted_orders:
            if order[1] == max_order:
                result.append(order[0])
            else:
                break
    
    return sorted(result)