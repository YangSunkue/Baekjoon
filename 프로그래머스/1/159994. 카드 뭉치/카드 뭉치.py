from collections import deque

def solution(cards1, cards2, goal):

    cards1 = deque(cards1)
    cards2 = deque(cards2)

    result = 'No'
    for g in goal:

        if cards1 and cards1[0] == g:
            cards1.popleft()
        elif cards2 and cards2[0] == g:
            cards2.popleft()
        else:
            break
    else:
        result = 'Yes'
    
    return result