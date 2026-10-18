class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        lowerb = 1
        upperb = max(piles)

        while lowerb < upperb:

            k = (lowerb + upperb) // 2

            time = 0

            for i in piles:
                time += -(i // -k)

            if time > h:
                lowerb = k + 1
            else:
                upperb = k

        return lowerb