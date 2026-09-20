class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix suffix solution
        prefix = [1]
        suffix = [1] #identity in multiplicaton, 1st and last inert

        for i in range(1,len(nums)):
            
            prefix.append( prefix[i-1] * nums[i-1] )
            suffix.append( suffix[i-1] * nums[len(nums)-i])
        
        ##print (suffix)
        #print(prefix)
        
        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[-i-1])
        return result



        