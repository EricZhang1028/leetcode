# 13. Roman to Integer
# time: O(n), space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        pair = {
            "I": {"V", "X"},
            "X": {"L", "C"},
            "C": {"D", "M"}
        }
        value_dict = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        }
        
        res, n, i =  0, len(s), 0
        while i < n:
            c = s[i]
            if (c in pair) and (i < n-1) and (s[i+1] in pair[c]):
                res += value_dict[s[i+1]] - value_dict[c]
                i += 2
            else:
                res += value_dict[c]
                i += 1
        return res