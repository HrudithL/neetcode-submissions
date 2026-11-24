class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find the min seen and the max seen after that point
        # subtract for max profit
        minseen = prices[0]
        maxprofit = 0

        for i in prices:
            minseen = min(i, minseen)
            maxprofit = max(i-minseen, maxprofit)

        return maxprofit