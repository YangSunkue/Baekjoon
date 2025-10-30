import functools

def solution(numbers):
    
    def compare(a, b):
        t1 = str(a) + str(b)
        t2 = str(b) + str(a)
        
        return (t1 > t2) - (t1 < t2)
    
    numbers.sort(key=functools.cmp_to_key(compare), reverse=True)
    
    result = ''.join(map(str, numbers))
    return result if int(result) != 0 else '0'