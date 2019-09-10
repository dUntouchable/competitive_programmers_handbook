# To find a path from the upper-left corner to the lower-right
# corner of an n × n grid, such that we only move down and right. Each square
# contains a positive integer, and the path should be constructed so that the sum of
# the values along the path is as large as possible.
#
# 1st solution is by recursion
# 2nd solution is by dp
#

import time

max_sum = 0
max_subarr = []
count = 0

# recursion solution
def recur(arr, subarr, S, row, col):
    global count
    global max_sum
    global max_subarr
    count += 1
    if row > 4 or col > 4:
        return
    elif row == 4 and col == 4:
        if max_sum < S:
            max_sum = S
            max_subarr = subarr
        return
    if row + 1 < len(arr):
        recur(arr, subarr + [arr[row+1][col]], S + arr[row+1][col], row + 1, col)
    if col + 1 < len(arr):
        recur(arr, subarr + [arr[row][col+1]], S + arr[row][col+1], row, col + 1)

    return


# DP Solution
def largest_sum_of_paths(arr, val):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == 0 and j == 0:
                val[i][j] = arr[i][j]
            elif i == 0:
                val[i][j] = arr[i][j] + val[i][j-1]
            elif j == 0:
                val[i][j] = arr[i][j] + val[i-1][j]
            else:
                val[i][j] = arr[i][j] + max(val[i][j-1], val[i-1][j])
        #print(val[i])
    return val

def print_path(arr, val):
    row, col = len(val)-1, len(val[0])-1
    subarr = [arr[row][col]]
    while row != 0 or col != 0:
        if row == 0:
            col -= 1
        elif col == 0:
            row -= 1
        elif val[row-1][col] < val[row][col-1]:
            col -= 1
        else:
            row -= 1
        subarr.insert(0, arr[row][col])

    print(sum(subarr), subarr)

arr = [[3,7,9,2,7], [9,8,3,5,5], [1,7,9,8,5], [3,8,6,4,10], [6,3,9,7,8]]
start_time = time.time()
recur(arr, [3], 3, 0, 0)
print("max_sum=",max_sum," count=",count," time taken= %0.7f" %(time.time() - start_time)," max_subarr=",max_subarr)

val = [[0 for _ in range(5)] for _ in range(5)]
#start_time = time.time()
val = largest_sum_of_paths(arr, val)
print_path(arr, val)
