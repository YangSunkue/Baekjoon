def solution(people, limit):
    
    """
    가장 무거운 사람과 가장 가벼운 사람을 함께 태운다
    """
    people.sort()
    left, right = 0, len(people) - 1
    
    result = 0
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            
        right -= 1
        result += 1
    
    return result