class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniques = []
        for i in range(len(nums)):
            if nums[i] in uniques:
                return True
            uniques.append(nums[i]) 
            
        return False