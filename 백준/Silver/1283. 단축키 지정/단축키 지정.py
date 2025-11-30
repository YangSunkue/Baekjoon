import sys
input = sys.stdin.readline

N = int(input())

visited = set()
for _ in range(N):

    string = input().strip()
    words = string.split(' ')

    break_flag = False
    # 1. 단어의 첫 알파벳 확인
    for i in range(len(words)):

        if words[i][0].upper() not in visited:
            visited.add(words[i][0].upper())
            key = ''
            for j in range(len(words)):
                if i == j:
                    key += '[' + words[j][0] + ']'
                    key += words[j][1:]
                else:
                    key += words[j]
                key += ' '

            print(key)
            break_flag = True    
        if break_flag: break
    if break_flag: continue
    
    # 2. 왼쪽부터 모든 알파벳 확인
    for i in range(len(words)):
        for j in range(len(words[i])):

            if words[i][j].upper() not in visited:
                visited.add(words[i][j].upper())
                key = ''
                for k in range(len(words)):
                    for l in range(len(words[k])):
                        if i == k and j == l:
                            key += words[k][:l]
                            key += '[' + words[k][l] + ']'
                            key += words[k][l + 1:]
                            key += ' '
                            break
                    else:
                        key += words[k]
                        key += ' '

                print(key)
                break_flag = True
            if break_flag: break
        if break_flag: break
    if break_flag: continue

    # 3. 어떠한 것도 단축키로 지정할 수 없는 경우
    print(string)
