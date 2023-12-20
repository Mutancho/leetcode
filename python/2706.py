def buyChoco(prices: list[int], money: int) -> int:
    prices.sort()
    return money - (prices[1] + prices[0]) if money - (prices[1] + prices[0]) >= 0 else money
