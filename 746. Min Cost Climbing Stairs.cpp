class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        if(cost.empty()) 
            return 0;
        for (int i = 2; i < cost.size(); i++) {
            cost[i] += min(cost[i-2], cost[i-1]);
        }
        return min(cost[cost.size()-1],cost[cost.size()-2]);
    }
};
