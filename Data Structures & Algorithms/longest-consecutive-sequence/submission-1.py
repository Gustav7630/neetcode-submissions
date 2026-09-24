class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        fast = set(nums)
        starts = set()
        longest = 0
        size = 1


        for n in nums:
            size = 1
            if n-1 in fast or n in starts:
                continue
            starts.add(n)
            x = n
            while x+1 in fast:
                x +=1
                size +=1
            if(size > longest):
                longest = size

        return longest
                
            
            
            