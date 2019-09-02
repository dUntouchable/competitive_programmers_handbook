# Counting Sort
# Time Complexity - O(n)
import random

def countingSort(arr):
    bookkeeping = [0] * (max(arr) + 1)
    for index in range(len(arr)):
        bookkeeping[arr[index]] += 1
    index = 0
    c = []
    while(index < len(bookkeeping)):
        if bookkeeping[index] != 0:
            c += [index] * bookkeeping[index]
        index += 1
    return c
    #return [[i]*var for i, var in enumerate(bookkeeping) if var != 0]

def checkAscending(arr):
    print(arr)
    if arr == sorted(arr):
        print("Counting sort - List in ascending order")
    else:
        print("Counting sort - List not in ascending order")

arr = []
for _ in range(10):
    arr.append(random.randint(1, 10))
print(arr)
checkAscending(countingSort(arr))
