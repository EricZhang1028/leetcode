# 11. Container With Most Water
# time: O(n), space: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l_ptr, r_ptr, max_capa = 0, len(height)-1, 0
        
        while l_ptr < r_ptr:
            min_heig = min(height[l_ptr], height[r_ptr])
            max_capa = max(max_capa, (r_ptr - l_ptr) * min_heig)
            
            if height[l_ptr] < height[r_ptr]:
                capa = (r_ptr - l_ptr) * height[l_ptr]
                l_ptr += 1
            else:
                capa = (r_ptr - l_ptr) * height[r_ptr]
                r_ptr -= 1
            max_capa = max(max_capa, capa)
            
        return max_capa