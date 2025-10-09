from collections import defaultdict

def solution(enroll, referral, sellers, amount):
    """
    10%를 윗사람에게 준다.
    10% 계산은 각 소득마다 별개이다.
    소수점은 버린다.

    enroll: 루트 제외한 모든 노드
    referral: enroll의 i번째 있는 노드의 부모 ('-' 일 경우 부모가 루트)
    seller: amount의 i번째 값이 어느 노드의 판매량인지
    amount: 판매량 목록 (1~100)
    """

    def distribute(seller, money):

        # root는 돈을 계산할 필요도 없고 부모도 없음
        if seller == '-':
            return

        m = money // 10
        if m >= 1:
            # 10% 나눠줄 수 있으면 90% 내가 먹고 10% 나눠줌
            money_dict[seller] += money - m

            idx = idx_dict[seller]
            parent = referral[idx]

            distribute(parent, m)
        else:
            # 못 나눠주면 내가 100% 먹음
            money_dict[seller] += money
            return
        
    idx_dict = dict()  # john: 0, mary: 1 ...
    money_dict = defaultdict(int)  # john: 100, mary: 350 ...

    for i, name in enumerate(enroll):
        idx_dict[name] = i

    # 수익 분배 메인 로직
    for i, seller in enumerate(sellers):
        money = amount[i] * 100
        distribute(seller, money)
    
    # 결과 생성
    result = []
    for name in enroll:
        result.append(money_dict[name])
    
    return result