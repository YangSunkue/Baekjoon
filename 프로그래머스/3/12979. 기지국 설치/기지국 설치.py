import math

def solution(n, stations, w):

    result = 0

    front = stations[0] - w - 1
    back = n - (stations[-1] + w)
    if front > 0:
        result += math.ceil(front / ((w * 2) + 1))
    if back > 0:
        result += math.ceil(back / ((w * 2) + 1))

    for i in range(1, len(stations)):

        left_range = stations[i - 1] + w
        right_range = stations[i] - w

        empty = right_range - left_range - 1
        if empty > 0:
            result += math.ceil(empty / ((w * 2) + 1))

    return result