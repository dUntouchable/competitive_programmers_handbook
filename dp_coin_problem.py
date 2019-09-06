#
# dp coin problem ##
#
# Q: Given a set # of coin values coins = { c 1 , c 2 , . . . , c k } and a target sum of money n , our task is to
# form the sum n using as few coins as possible.
#
import math

def solve(total, coins, arr):
    if total < 0:
        return math.inf
    elif total == 0:
        return 0

    if arr[total] != 0:
        return arr[total]

    min_coins = total + 1
    for i in range(len(coins)):
        min_coins = min(min_coins, solve(total - coins[i], coins, arr) + 1)

    arr[total] = min_coins
    return min_coins

coins = [1, 3, 4]
total = 10
arr = [0]*(total+1)
_ = solve(total, coins, arr)
for i,var in enumerate(arr):
    print('solve(', i, ') = ', var)
