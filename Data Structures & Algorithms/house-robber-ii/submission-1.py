class Solution:
    def rob(self, nums: List[int]) -> int:
        v2 = nums[0]
        if len(nums) < 2:
            return v2 
        v1 = max(v2,nums[1]) # best at leftmost -1
        if len(nums) < 3:
            return max(v1,v2) 
        
        def straight_rob(nums):
            v2 = nums[0] # leftmost val
            if len(nums) < 2:
                return v2 
            v1 = max(v2,nums[1]) # best at leftmost -1
            if len(nums) < 3:
                return max(v1,v2) 

            for i in range(2,len(nums)):
                temp = v1
                v1 = max(v2 + nums[i], v1 )
                v2 = temp
            return v1
        xstart = straight_rob(nums[1:])
        xend = straight_rob(nums[:-1])
        return max(xstart,xend)