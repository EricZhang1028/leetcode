# 03. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        left, right, max_res = 0, 0, 0

        while right < len(s):
            chars[ord(s[right])] += 1
            
            while chars[ord(s[right])] > 1:
                chars[ord(s[left])] -= 1
                left += 1

            max_res = max(max_res, right - left + 1)
            right += 1
        
        return max_res