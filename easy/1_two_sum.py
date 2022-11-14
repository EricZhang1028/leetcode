# 01. two sum
# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {} # element: index --> key: value
        
        for i in range(len(nums)):
            sub_res = target - nums[i]
            if sub_res in hash_table:
                return [hash_table[sub_res], i]
            else:
                hash_table[nums[i]] = i
        
        return []