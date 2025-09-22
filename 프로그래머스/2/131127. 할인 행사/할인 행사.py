from collections import defaultdict

def solution(want, number, discount):

    def is_ok(w_n):
        for key in want:
            if w_n[key] != 0:
                return False
        return True

    want_number = defaultdict(int)
    for i in range(len(want)):
        want_number[want[i]] = number[i]

    # 첫 10개 날은 미리 빼놓음
    result = 0
    for i in range(10):
        want_number[discount[i]] -= 1
    if is_ok(want_number):
        result += 1

    # 슬라이딩 윈도우
    for i in range(10, len(discount)):
        want_number[discount[i]] -= 1
        want_number[discount[i - 10]] += 1

        if is_ok(want_number):
            result += 1
    
    return result