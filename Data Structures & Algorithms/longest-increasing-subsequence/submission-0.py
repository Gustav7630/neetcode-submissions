class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        subsequences = [] #stores tuples (max_len,max_val)
        res = 0
        prev_val = -1001 #guarenteed in problem spec less than -1000
        
        for i in range(len(nums)):
            cur_length = 0
            for j in range (len(subsequences)):
                if subsequences[j][1] < nums[i] and subsequences[j][0] > cur_length:
                    cur_length = subsequences[j][0]
            cur_length +=1
            if cur_length > res:
                res = cur_length
            subsequences.append((cur_length,nums[i]))
        print(subsequences)
        print(nums)
        return res