#
# Find all possible set of coins that has a sum of S
# 1st Solution Recursion and 2nd solution Memoization

# Recursion
#
def recur(coins, S, subarr):
    if S == 0:
        print(subarr)
        return 1
    elif S < 0:
        return 0
    total_count = 0
    for var in coins:
        total_count += recur(coins, S - var, subarr + [var])

    return total_count

# Memoization
#
def counting_solutions(coins, S):
    val = [0]*(S+1)
    val[0] = 1
    for index in range(1,S+1):
        for c in coins:
            if index >= c:
                val[index] += val[index-c]
    print(val[-1])

coins = [1,3,4]
print(recur(coins, 5, []))
print('---------')
counting_solutions(coins, 5)
