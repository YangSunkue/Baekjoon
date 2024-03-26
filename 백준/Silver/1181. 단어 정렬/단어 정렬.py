import sys

wordList = []
for i in range(int(sys.stdin.readline())):
    wordList.append(sys.stdin.readline().strip())

setList = set(wordList) # 중복 제거
sortedList = sorted(setList, key = lambda x: (len(x), x)) # 길이 순으로 먼저 정렬 후 알파벳 순으로 정렬

for i in sortedList:
    print(i)