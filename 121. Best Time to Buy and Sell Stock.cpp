class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int buy;
        int sell=0;
        if(prices.empty())
            return 0;
        buy = numeric_limits<int>::min();
        for ( auto i : prices ) {
            buy = max(buy, -i);
            sell = max(sell, buy+i);
        }
        return sell;
    }
};
