def solution(array, commands):
    
    def slice_and_sort(s, e):
        return sorted(array[s - 1 : e])
    
    result = []
    for cmd in commands:
        result.append(slice_and_sort(cmd[0], cmd[1])[cmd[2] - 1])

    return result