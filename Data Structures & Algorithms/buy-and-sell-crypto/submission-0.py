class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = 100
        res = 0;
        for price in prices:
            if price < min_buy:
                min_buy = price
            res = max(res, price - min_buy)
        return res




        