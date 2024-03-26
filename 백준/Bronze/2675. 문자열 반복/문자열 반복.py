for i in range(int(input())):
    r, s = input().split()
    result = ''
    
    for j in s:
        result += j*int(r)
    print(result)