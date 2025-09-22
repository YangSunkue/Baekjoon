def solution(record):

    user_dict = dict()

    # 유저id와 닉네임을 매핑 (마지막 기준)
    for re in record:

        if re.startswith('Enter') or re.startswith('Change'):
            _, user, nickname = re.split(' ')
            user_dict[user] = nickname
    
    # 결과 생성
    result = []
    for re in record:

        if re.startswith('Leave'):
            _, user = re.split(' ')
            string = f'{user_dict[user]}님이 나갔습니다.'
            result.append(string)
        
        elif re.startswith('Enter'):
            _, user, _ = re.split(' ')
            string = f'{user_dict[user]}님이 들어왔습니다.'
            result.append(string)
    
    return result