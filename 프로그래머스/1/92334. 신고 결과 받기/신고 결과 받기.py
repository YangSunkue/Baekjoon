from collections import defaultdict

def solution(id_list, report, k):

    """
    한 명을 한 번씩만 신고 가능
    """

    attack_dict = defaultdict(list)  # 신고자: [대상자1, 대상자2 ..]
    reported_dict = defaultdict(int) # 대상자: 신고횟수

    # 중복 신고 제거
    report = list(set(report))

    for re in report:
        attacker, reported = re.split(' ')

        attack_dict[attacker].append(reported)
        reported_dict[reported] += 1
    
    fires = defaultdict(int)  # [정지자1, 정지자2 ..]
    for reported in reported_dict:
        if reported_dict[reported] >= k:
            fires[reported] = 1

    result = []
    for user in id_list:
        count = 0
        for reported in attack_dict[user]:
            if fires[reported] == 1:
                count += 1
        
        result.append(count)
    
    return result