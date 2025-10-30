import functools

def solution(numbers):

    def compare(a, b):
        s1 = a + b
        s2 = b + a

        return (s1 > s2) - (s1 < s2)
    
    numbers = list(map(str, numbers))
    numbers.sort(key=functools.cmp_to_key(compare), reverse=True)

    result = ''.join(numbers)

    return result if int(result) != 0 else '0'