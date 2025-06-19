import sys
input = sys.stdin.readline

"""
모음 반드시 1개 이상 포함: a, e, i, o, u
같은 글자는 연속 안됨. but 예외: ee, oo
모음 또는 자음은 연속 2개까지만
"""

def is_safe(password):

    mos = 'aeiou'

    # 모음을 1개 이상 포함하는지
    include_mo = False
    for p in password:
        if p in mos:
            include_mo = True
            break
    if not include_mo:
        return False
    
    # 길이가 1일 경우, 모음만 포함하면 True
    if len(password) == 1:
        return True


    # 같은 글자가 연속되는지 확인 -> ee, oo 는 예외
    left = 0
    right = left + 2
    while right <= len(password):
        text = password[left:right]

        if text[0] == text[1]:
            if text != 'ee' and text != 'oo':
                return False
        
        left += 1
        right += 1
    
    # 모음 또는 자음이 3번 연속되지 않는지 확인
    if len(password) >= 3:

        left = 0
        right = left + 3
        while right <= len(password):

            text = password[left:right]
            mo = 0
            za = 0

            for t in text:
                if t in mos:
                    mo += 1
                else:
                    za += 1

            if mo == 3 or za == 3:
                return False
            
            left += 1
            right += 1

    # 조건을 전부 통과하면 return
    return True


while True:

    password = input().strip()
    if password == 'end':
        break
    
    # 검사 결과에 따라 메시지 생성
    message = '<' + password + '> '
    if is_safe(password):
        message += 'is acceptable.'
    else: message += 'is not acceptable.'

    print(message)