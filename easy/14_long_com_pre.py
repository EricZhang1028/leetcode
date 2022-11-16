# 14. Longest Common Prefix
# time: O(S), space: O(1)

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lg_pre = strs[0]

        for s in strs:
            lg_pre = lg_pre[:min(len(lg_pre), len(s))]
            for i in range(len(lg_pre)):
                if lg_pre[i] != s[i]:
                    lg_pre = lg_pre[:i]
                    break

        return lg_pre