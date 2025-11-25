def solution(numbers):
    
    result = int(-1e9)
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            result = max(result, numbers[i] * numbers[j])
    return result