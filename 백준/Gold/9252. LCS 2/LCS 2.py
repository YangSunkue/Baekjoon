import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

n = len(str1)
m = len(str2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

# dp 테이블 제작
for i in range(1, m + 1):
    for j in range(1, n + 1):

        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# LCS 문자열 역추적
string = []
i, j = m, n
while i > 0 and j > 0:

    if str2[i - 1] == str1[j - 1]:
        string.append(str2[i - 1])
        i -= 1
        j -= 1
    
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(dp[m][n])
print(''.join(reversed(string)))