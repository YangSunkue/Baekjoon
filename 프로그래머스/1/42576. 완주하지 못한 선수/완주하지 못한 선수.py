from collections import defaultdict

def solution(part, comp):

    how_many = defaultdict(int)
    for c in comp:
        how_many[c] += 1

    for p in part:
        if how_many[p] == 0:
            return p
        
        how_many[p] -= 1