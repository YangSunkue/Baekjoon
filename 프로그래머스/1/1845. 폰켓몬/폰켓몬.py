def solution(nums):

    monsters = set()
    for num in nums:
        monsters.add(num)
    
    max_count = len(nums) // 2
    count = len(monsters)
    
    return min(max_count, count)