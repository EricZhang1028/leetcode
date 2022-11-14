# 5. Longest Palindromic Substring
# time: O(n^2), space: O(n^2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l, res_r, n = 0, 0, len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if i == j: 
                    dp[i][j] = True
                elif j-i == 1:
                    dp[i][j] = True if s[i] == s[j] else False
                else:
                    dp[i][j] = True if s[i] == s[j] and dp[i+1][j-1] else False
                  
                if dp[i][j] and (res_r-res_l) < (j-i):
                    res_l, res_r = i, j
        
        return s[res_l:res_r+1]