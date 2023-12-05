def maxProfit(prices: list[int]) -> int:
    output = 0
    for i in range(1, len(prices)):
        if prices[i] - prices[i - 1] > 0:
            output += prices[i] - prices[i - 1]
    return output


print(maxProfit([7, 1, 5, 3, 6, 4]))
