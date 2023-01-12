prices = [7, 1, 2, 3, 4, 6, 5]

res = 0
max = 0
bought = False
for i in range(len(prices)):
    if bought:
        if max < prices[i]:
            max = prices[i]
    else:
        if max < prices[i]:
            max = prices[i]

