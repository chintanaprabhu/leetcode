class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty())
            return 0;
        int profit=0, buy=prices[0];
        for (int price : prices) {
            buy = min(price,buy);
            //int cur_profit = price-buy;
            profit = max(price-buy,profit);       
        }
        return profit;
    }
};
