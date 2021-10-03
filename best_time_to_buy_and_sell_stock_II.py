from typing import List


prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]


def maxProfit(prices:List[int]) -> int:
    """
    :type prices: List[int]
    :rtype: int
    """
    profit_list = []
    previous = prices[0]

    for price in prices[1:]:
        profit = price - previous
        if profit > 0:
            profit_list.append(profit)
        previous = price

    return sum(profit_list)


print(maxProfit(prices))
