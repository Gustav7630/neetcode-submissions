class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        stones = list(map(lambda x: -x,stones))
        heapq.heapify(stones)
        print(stones)

        while len(stones) >1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            newStone = -abs( stone1 - stone2)
            if newStone !=0:
                heapq.heappush(stones,newStone)
        
        if(len(stones) == 1):
            return stones[0] * -1
        return 0