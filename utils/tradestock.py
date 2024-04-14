class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # 双指针
        profit_list = []
        befor_pointer = 0
        while befor_pointer < len(prices):
            for after_pointer in range(befor_pointer, len(prices)):
                if prices[after_pointer] > prices[befor_pointer]:
                    profit_list.append(prices[after_pointer] - prices[befor_pointer])
            befor_pointer += 1
        if len(profit_list) == 0:
            return 0
        else:
            return max(profit_list)