from typing import List

class Solution:
    def price_of_affordable_gun(self, wallet: int, prices: List[int]) -> int:
        affordable_price = 0
        for price in prices:
            if wallet - price > 0 and \
                price > affordable_price:
                affordable_price = price
        return affordable_price

_, wallet = map(int, input().split(' '))
prices = list(map(int, input().split(' ')))
solution = Solution()
print(solution.price_of_affordable_gun(wallet, prices))
