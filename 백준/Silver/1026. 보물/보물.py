import sys
input = sys.stdin.readline

# N 입력받기
N = int(input())
# a 입력받고 내림차순 정렬
a = list(map(int, input().split()))
a.sort(reverse=True)
# b 입력받기
b = list(map(int, input().split()))

result = 0
for i in a:
    bIndex = b.index(min(b))
    bValue = b.pop(bIndex)
    result += i * bValue

print(result)