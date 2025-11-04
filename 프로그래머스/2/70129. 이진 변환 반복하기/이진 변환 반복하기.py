def solution(s):

    def to_binary(num):
        num = int(num)
        result = []

        while True:
            result.append(num % 2)
            if num == 1:
                break
            num //= 2
        
        result.reverse()
        return ''.join(map(str, result))

    changed_cnt = 0
    deleted_zero = 0
    while s != '1':

        deleted = s.count('0')
        s = to_binary(len(s) - deleted)

        deleted_zero += deleted
        changed_cnt += 1
    
    return [changed_cnt, deleted_zero]