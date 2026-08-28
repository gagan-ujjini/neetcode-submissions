class Solution {
    public int maxProfit(int[] prices) {
        int l=0, profit=0, maxProfit=0;
        for(int r=1;r<prices.length;r++){
            if(prices[r] > prices[l]){
                profit = prices[r] - prices[l];
                maxProfit = Math.max(profit, maxProfit);
            } else {
                l = r;
            }
        }
        return maxProfit;
    }
}
