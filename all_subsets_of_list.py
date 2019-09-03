#
# Print all subsets of a list
#
# Total number of subsets are 2^n for an array of length n
# The logic is to use recursion, and to utilize two choices at every step.
# Choice 1 is to keep it Null for an index
# Choice 2 is to keep use the value of arr of index index
#

def helper(arr, subset, i):
    if i == len(arr):
        print([var for var in subset if var != None])
    else:
        subset[i] = None
        helper(arr, subset, i+1)
        subset[i] = arr[i]
        helper(arr, subset, i+1)

def allSubsets(arr):
    subset = [0] * len(arr)
    helper(arr, subset, 0)


arr = [1,2,3]
allSubsets(arr)
