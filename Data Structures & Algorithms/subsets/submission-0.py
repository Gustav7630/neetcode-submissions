class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def backtrack(index,choices):
            if index == len(nums):
                #print(choices)
                res.append(choices.copy())#need to resolve pass by reference
                #print(res)
                return 
            #decision 1, include the current index
            choices.append(nums[index])
            #print(choices)
            backtrack(index+1,choices)
            choices.pop()

            #decision 2, dont include

            backtrack(index+1,choices)

        backtrack(0,[])
        return res
