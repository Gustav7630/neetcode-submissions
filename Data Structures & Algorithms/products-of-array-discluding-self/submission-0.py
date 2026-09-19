class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        oCount = 0
        for n in nums:
            if n == 0:
                oCount +=1
            else:
                total *= n
        
        if oCount >1:
            total = 0

        
        result = []
        for n in nums:
            if(n ==0):
                result.append(total)
            elif oCount ==0:
                result.append(int(total/n))
            else:
                result.append(0)
        
        return result