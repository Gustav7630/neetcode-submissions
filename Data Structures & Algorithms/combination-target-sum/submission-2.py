class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        #need to keep adding untill we cross total, then change index and do the same

        res = []

        def backtrack(index,choices,total):
            #base case

            if total >= target or index == len(nums):
                if(total == target ):#and choices not in res
                    res.append(choices.copy())
                    
                return
    
            choices.append(nums[index])
            total += nums[index]
            #backtrack(index +1,choices,total)
            backtrack(index,choices,total)


            total -=nums[index]
            choices.pop()
            backtrack(index+1,choices,total)
        
        backtrack(0,[],0)
        
        return res