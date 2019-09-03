#
# Generating Permutations
#

def permute(arr, l):
    if l == len(arr):
        print(arr)
        return
 
    for i in range(l, len(arr)):
        arr[i], arr[l] = arr[l], arr[i]
        permute(arr, l+1)
        arr[i], arr[l] = arr[l], arr[i]

arr = [1,2,3]
permute(arr, 0)
