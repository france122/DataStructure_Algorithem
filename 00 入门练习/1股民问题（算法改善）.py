#!/user/bin/env python3
# -*- coding: utf-8 -*-
# 交易一次
def max_profit_one_deal(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit

    return max_profit

prices = list(map(int, input().split()))
max_profit = max_profit_one_deal(prices)

print(max_profit)