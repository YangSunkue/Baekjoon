def solution(prices):

    """
    인덱스를 push, 첫주식 push 하고 시작

    현재값(인덱스)과 top을 비교해서:
    top보다 같거나 클 경우 push
    top보다 작을 경우 현재값 - top 값을 top의 길이로 확정

    순회 후, stack top은 무조건 0 확정
    남아있는 애들은 (len(prices) - 1) - 인덱스 로 확정
    """

    le = len(prices)
    result = [-1] * le

    stack = []
    stack.append(0)
    for i in range(1, le):

        cur_stock = prices[i]
        prev_stock = prices[stack[-1]]

        # 주식이 떨어졌을 경우
        while cur_stock < prev_stock and stack:

            result[stack[-1]] = i - stack[-1]
            stack.pop()
            
            if stack:
                prev_stock = prices[stack[-1]]
        
        stack.append(i)
    
    # 맨 마지막 주식은 무조건 0
    result[stack.pop()] = 0

    # 끝까지 살아남은 주식들
    while stack:
        strong_stock = stack.pop()
        result[strong_stock] = (le - 1) - strong_stock
    
    return result