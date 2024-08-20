def makeChange(coins, total):
    if total <= 0:
        return 0
    else:
        coin = sorted(coins, reverse=True)
        counter = 0
        for i in coin:
            while total >= i:
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1