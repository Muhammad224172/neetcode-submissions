class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ones = []
        for i in nums:
            if i not in ones:
                ones.append(i)
        if len(ones) < len(nums):
            return True 
        else:
            return False 