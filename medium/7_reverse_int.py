# 7. Reverse Integer
# time: O(n), space: O(1)

class Solution:
    def reverse(self, x: int) -> int:
        a = -x if x < 0 else x
        
        rev = 0
        while a != 0:
            pop = a % 10
            a = a // 10
            rev = rev * 10 + pop
            
        if x < 0:
            rev *= -1
        
        if rev > pow(2, 31)-1 or rev < -pow(2, 31):
            return 0
        else:
            return rev