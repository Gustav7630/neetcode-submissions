class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        sum_costs = len(cost) * [0]
        sum_costs[0] = cost[0]
        sum_costs[1] = cost[1]

        for i in range(2,len(cost)):
            sum_costs[i] = min(sum_costs[i-1],sum_costs[i-2]) + cost[i]
        
        #print(sum_costs)
        return min(sum_costs[-1],sum_costs[-2])