# this is optimized solution than greedy approach. for example, for [1,4,5] target 13 greedy approach will give me 5 coins, but this approach will give me only 3 coins (4+4+5) 

memo = {}

def min_ignore_none(a, b):
    if a is None:
        return b
    if b is None:
        return a 
    return min(a,b)

def minimum_coins(target, coins):
    if target in memo:
        return memo[target]
    if target == 0:
        answer = 0 
    else:
        answer = None
        for coin in coins:
            subproblem = target - coin
            if subproblem < 0:
                # skip solution whre we try to reach [target] from a negative subproblem
                continue
            answer =  min_ignore_none(answer, minimum_coins(subproblem, coins)+1)
    memo[target] = answer
    return answer

print(minimum_coins(131, [1,4,5]))