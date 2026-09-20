class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1 #front
            k = len(nums)-1 #back
           
            while j < k:
                ans = -(nums[j] + nums[k])
            # print(f"ans = {ans} -({nums[j]} -{nums[k]}) i = {nums[i]}")
                if nums[i] == ans:
                    result.append([nums[i],nums[j],nums[k]])
                    temp = nums[j]
                # while j< len(nums)and nums[j] == temp: #avoid dupes
                #      j +=1
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif ans < nums[i]:
                    k -=1
                else:
                    j += 1



                
        
        return result
