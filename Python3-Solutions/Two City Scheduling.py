class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        costs.sort(key=lambda x: x[0]-x[1]) #sort the list wrt the difference between price_a and price_b
        for i in range(len(costs)):
            if i <= len(costs)/2-1:
                min_cost += costs[i][0]
            else:
                min_cost += costs[i][1]
        return min_cost
            
