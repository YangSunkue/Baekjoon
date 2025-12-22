import sys
input = sys.stdin.readline

string = input().strip()
le = len(string)

def is_palindrom(sub_str):
    
    l = 0
    r = len(sub_str) - 1
    while l < r:
        if sub_str[l] != sub_str[r]:
            return False
        l += 1
        r -= 1
    
    return True

for i in range(le):
    if is_palindrom(string[i:]):
        print(le + i)
        break