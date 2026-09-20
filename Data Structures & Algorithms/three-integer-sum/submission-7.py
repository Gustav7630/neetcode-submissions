class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                current = nums[j] + nums[k]

                if current == -nums[i]:
                    result.append([nums[i], nums[j], nums[k]])

                    
                    j += 1
                    k -= 1

                    #avoid dupes
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif current > -nums[i]:
                    k -= 1
                else:
                    j += 1

        return result