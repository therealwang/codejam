import sys
import numpy as np

def main():
    cases = int(sys.stdin.readline())
    for case in range(cases):
        str1 = sys.stdin.readline().strip()
        str2 = sys.stdin.readline().strip()
        print 'Case #{}: {}'.format(case + 1, findPoss(str1,str2))
        

def findPoss(str1, str2):
    dp = np.zeros([len(str1), len(str2)])
    for i in range(len(str1)):
        for j in range(len(str2)):
            if i == j == 0:
                if str1[i] == str2[j]:
                    dp[0][0] = 0
                elif str1[i] == '*' or str2[j] == '*':
                    dp[0][0] = 1
                else:
                    return False
            else:
                best = min(diagcand(str1,str2,i,j,dp),rowcand(str1,str2,i,j,dp),colcand(str1,str2,i,j,dp))
                dp[i][j] = best if best <= 4 else -1

    return dp[len(str1)-1][len(str2)-1] >= 0

def diagcand(str1,str2,i,j,dp):
    if i == 0 or j == 0:
        return 100
    elif dp[i-1][j-1] >= 0:
        if str1[i] == str2[j]:
            return 0
        elif str1[i] == '*' or str2[j] == '*':
            return 1
        else:
            return 100
    else:
        return 100

def rowcand(str1,str2, i, j, dp):
    if j == 0:
        return 100
    elif str1[i] == '*' and 0 <= dp[i][j-1] <= 4:
        if str2[j] == '*':
            return dp[i][j-1]
        else:
            return dp[i][j-1]+1
    elif str2[j-1] == '*' and 0 <= dp[i][j-1] <= 4:
        if str2[j] == str1[i]:
            return 0
        elif str2[j] == '*' or str1[i] == '*':
            return 1
        else:
            return 100
    elif str2[j] == '*':
        return dp[i][j-1] if dp[i][j-1] >= 0 else 100
    else:
        return 100
    

def colcand(str1,str2,i,j,dp):
    if i == 0:
        return 100
    elif str2[j] == '*' and 0 <= dp[i-1][j] <= 4:
        if str1[i] == '*':
            return dp[i-1][j]
        else:
            return dp[i-1][j]+1
    elif str1[i-1] == '*' and 0 <= dp[i-1][j] <= 4:
        if str2[j] == str1[i]:
            return 0
        elif str2[j] == '*' or str1[i] == '*':
            return 1
        else:
            return 100
    elif str1[i] == '*':
        return dp[i-1][j] if dp[i-1][j] >= 0 else 100
    else:
        return 100

main()
