def buy_and_sell_stocks():
    prices = [2,4,1]
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        profit = price - min_price

        print(profit)
        if profit > max_profit:
            max_profit = profit

    return max_profit


