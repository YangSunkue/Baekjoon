from collections import defaultdict

def solution(k, tangerines):

    size_to_num = defaultdict(int)
    for tangerine in tangerines:
        size_to_num[tangerine] += 1
    size_to_num = sorted(size_to_num.items(), key=lambda x: -x[1])

    t = set()
    count = 0
    for size, num in size_to_num:
        t.add(size)

        if count + num < k:
            count += num
            continue
        else:
            break
    
    return len(t)