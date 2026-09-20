class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        res = 0
        while right > left:
            height = min(heights[left],heights[right])
        
            area = (right - left) * height
            res = max(res,area)

            if heights[left] > heights[right]:
                right -=1
            else:
                left += 1
        #want the biggest pair so incrament the smaller one 

        return res

        
        

