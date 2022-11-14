# 6. Zigzag Conversion
# time: O(n), space: O(n)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res_li = [[] for _ in range(numRows)]
        
        goingDown, i = False, 0
        for c in s:
            res_li[i].append(c)
            
            if (i == numRows-1) or (i == 0):
                goingDown = not goingDown
            
            i = i+1 if goingDown else i-1
            
        res = ""
        for row in res_li:
            res += "".join(row)
            
        return res