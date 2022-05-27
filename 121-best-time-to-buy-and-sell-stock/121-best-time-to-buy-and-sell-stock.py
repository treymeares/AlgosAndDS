class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_ = 0
        left = 0
        right = 1
        while right < len(prices):
            if prices[left] < prices[right]:
                current_max = prices[right] - prices[left]
                max_ = max(current_max, max_)
                right += 1
            else:
                left = right
                right += 1
        return max_