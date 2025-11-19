def solution(people, limit):
    
    """
    10 20 30 70 80 80
    """
    
    people.sort()
    
    result = 0
    left, right = 0, len(people) - 1
    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1
            
        right -= 1
        result += 1
    
    return result