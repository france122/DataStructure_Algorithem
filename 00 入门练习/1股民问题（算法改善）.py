# 允许交易一次
def max_profit_one_deal(prices):
    if not prices:
        return 0

    in_price = out_profit = prices[0]
    max_profit = 0

    for price in prices:
        if price < in_price:
            in_price = price
            out_profit = 0
        elif price > out_profit:
            out_profit = price
            if out_profit - in_price > max_profit:
                max_profit = out_profit - in_price


    return max_profit


# 示例用法
prices = list(map(int, input().split()))
max_profit = max_profit_one_deal(prices)

print(max_profit)
