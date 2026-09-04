class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for i in nums:
            if i in frequencies:
                frequencies[i] += 1
            else:
                frequencies[i] = 1

        buckets = []

        for i in range(len(nums) + 1):
            buckets.append([])

        for value in frequencies:
            frequency = frequencies[value]
            buckets[frequency].append(value)

        count = 0
        index = len(nums)
        result = []

        
        while count < k:
            
            for j in range(len(buckets[index])):
                
                result.append(buckets[index][j])
                count +=1
                if count == k:
                    break
            index = index -1
            if count == k:
                break
            
        return result

        
            