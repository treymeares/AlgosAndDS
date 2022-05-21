class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count, prev = 0, 1 << amount
        print(prev)
        while prev & 1 == 0:
            cur = prev
            for coin in coins:
                cur |= prev >> coin
            if cur == prev:
                return -1
            count += 1
            prev = cur
        return count