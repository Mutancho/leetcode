def maxProfit(prices: list[int]) -> int:
    output = 0
    min_val = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < min_val:
            min_val = prices[i]
        else:
            diff = prices[i] - min_val
            if diff > 0 and diff > output:
                output = diff
    return output


print(maxProfit([7, 1, 5, 3, 6, 4]))
