class Solution:
    def rob(self, nums: List[int]) -> int:
        if(len(nums) ==1):
            return nums[0]


        sums = len(nums) * [0]
        sums[0] = nums[0]
        sums[1] = nums[1]
        count = 0
        for i in range(len(nums)-3):
            count +=1
            plustwo = sums[i] + nums[i+2]
            plusthree = sums[i] + nums[i+3]

            sums[i+2] = max(sums[i+2],plustwo)
            sums[i+3] = max(sums[i+3],plusthree)
        if(count + 2 < len(nums)):
            plustwo = sums[count] + nums[count+2]
            sums[count+2] = max(sums[count+2],plustwo)
        return max(sums[-1],sums[-2])