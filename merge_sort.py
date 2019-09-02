# Merge Sort
import random, sys

def merge(a, b):
    a_1 = a + [sys.maxint]*len(b)
    b_1 = b + [sys.maxint]*len(a)
    a_ind, b_ind = 0, 0
    c = []
    for _ in range(len(a_1)):
        if a_1[a_ind] < b_1[b_ind]:
            c.append(a_1[a_ind])
            a_ind += 1
        else:
            c.append(b_1[b_ind])
            b_ind += 1
    return c

def mergeSort(arr):
    if len(arr) == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    elif len(arr) <= 1:
        return arr

    a = mergeSort(arr[:len(arr)/2])
    b = mergeSort(arr[len(arr)/2:])
    return  merge(a, b)

def checkAscending(arr):
    print(arr)
    if arr == sorted(arr):
        print("Merged sort - List in ascending order")
    else:
        print("Merged sort - List not in ascending order")


arr = []
for _ in range(10):
    arr.append(random.randint(1, 100))
print(arr)
checkAscending(mergeSort(arr))
