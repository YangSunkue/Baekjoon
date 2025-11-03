def solution(elements):
    
    le = len(elements)
    elements = elements * 2
    
    values = set()
    for i in range(1, le + 1):
        
        left = 0
        right = left + i
        value = sum(elements[left:right])
        values.add(value)
        
        for _ in range(le - 1):
            value -= elements[left]
            left += 1
            right += 1
            value += elements[right - 1]
            
            values.add(value)
    
    return len(values)