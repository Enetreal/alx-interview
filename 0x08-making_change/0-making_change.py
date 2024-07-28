def makeChange(coins, total):
    if total <= 0:
        return 0

    else:
        coins.sort(reverse=True)
        counter = 0
        for coin in coins:
            while total >= coin:
                counter += 1
                total -= coin
        if total == 0:
            return counter
        return -1