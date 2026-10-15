class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        choice = 0
        res = []

        def backtrack(choice):
            
            if(choice == len(nums)):
                res.append(nums.copy())
            
            for i in range(choice,len(nums)):
                nums[choice],nums[i] = nums[i],nums[choice]
                backtrack(choice+1)
                nums[choice],nums[i] = nums[i],nums[choice]
            
            
        backtrack(0)
        
        return res