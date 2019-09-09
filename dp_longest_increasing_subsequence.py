#
# Longest increasing subsequence
# 
# 1st solution is by recursion
# 2nd solution is by memoization
#

import time

max_subarr = []
count = 0

def recur(arr, subarr):
    global count
    global max_subarr
    count += 1
    if not arr:
        if len(max_subarr) < len(subarr):
            max_subarr = subarr
        return

    recur(arr[1:], subarr)
    if not subarr or arr[0] > subarr[-1]:
        recur(arr[1:], subarr + [arr[0]])

def longest_increasing_subsequence(arr):
    val = [1]*len(arr)
    for i in range(len(val)):
        for j in range(i):
            if arr[j] < arr[i]:
                val[i] = max(val[i], val[j]+1)

    max_val = max(val)
    large_subsequence = []
    for i in range(len(val)-1, -1, -1):
        if val[i] == max_val:
            if not large_subsequence:
                large_subsequence.insert(0, arr[i])
                max_val -= 1
            elif arr[i] < large_subsequence[0]:
                large_subsequence.insert(0, arr[i])
                max_val -= 1
    print(large_subsequence)



arr = [6,2,5,1,7,4,8,3]
start_time = time.time()
recur(arr, [])
print(max_subarr)
elapsed_time = time.time() - start_time
print("Number of  time the recursion function called was ",count, " took %0.6f" %elapsed_time," secs")

start_time = time.time()
longest_increasing_subsequence(arr)
elapsed_time = time.time() - start_time
print("time taken for memoization function to complete %0.6f" %elapsed_time," secs")
