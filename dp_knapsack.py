#
# Knapsack problem
#
# Find all possible sums can be formed using the weights
#

def recur(arr, S, initial_sum):
    if S == 0:
        print(initial_sum, end=" ")
        return
    elif not arr:
        return
    elif S < 0:
        return
    recur(arr[1:], S-arr[0], initial_sum)
    recur(arr[1:], S, initial_sum)

def knapsack(arr, S):
    val_arr = [False]*(S+1)
    val_arr[0] = True
    for k in arr:
        for s in range(S,-1,-1):
            if val_arr[s]:
                val_arr[s + k] = True
    for i in range(1,S+1):
        if val_arr[i]:
            print(i,end=" ")

arr = [1,3,3,5]
S = sum(arr)
#for s in range(1,S+1):
#    recur(arr,s,s)
knapsack(arr, S)
