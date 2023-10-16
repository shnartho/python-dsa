def greedy_coin_change(coins, target_amount):
    coins.sort(reverse=True)
    coin_count = 0

    for coin in coins:
        while target_amount >= coin:
            target_amount -= coin
            coin_count += 1
    
    return coin_count

coins = [2, 5, 1]
target_amount = 14
min_coins = greedy_coin_change(coins, target_amount)
print(f"Minimum number of coins to make {target_amount} cents: {min_coins}")