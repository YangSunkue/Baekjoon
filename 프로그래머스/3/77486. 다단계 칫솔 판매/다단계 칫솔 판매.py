def solution(enroll, referral, seller, amount):

    parent_dict = (dict(zip(enroll, referral)))
    total_dict = {name: 0 for name in enroll}

    for i in range(len(seller)):

        money = amount[i] * 100
        cur_name = seller[i]

        while money > 0 and cur_name != '-':
            total_dict[cur_name] += money - (money // 10)
            cur_name = parent_dict[cur_name]
            money //= 10
    
    return [total_dict[name] for name in enroll]