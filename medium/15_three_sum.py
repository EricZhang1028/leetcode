class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = set()
        nums.sort()
        for i, v in enumerate(nums):
            if i>0 and v in nums[:i]: continue
            
            d = {}
            for x in nums[i+1:]:
               
                if x in d:
                    ret.add((v, x, -v-x))
                else:
                    d[-v-x] = 1
        
        return list(ret)
                    