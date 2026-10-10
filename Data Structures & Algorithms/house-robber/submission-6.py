class Solution:
    def rob(self, nums: List[int]) -> int:
        v2 = nums[0] # leftmost val
        if len(nums) < 2:
            return v2 
        v1 = max(v2,nums[1]) # best at leftmost -1

       # index = 0

        for i in range(2,len(nums)):
            temp = v1
            v1 = max(v2 + nums[i], v1 )
            v2 = temp
            #print(v1)
        
        return v1