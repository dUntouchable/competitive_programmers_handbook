arr = [-1, 2, 4, -3, 5, 2, -5, 2]

cur_sum = arr[0]
best = arr[0]
prev = arr[0]

for index in range(1, len(arr)):
    cur_sum = prev + arr[index]
    if arr[index] > cur_sum:
        cur_sum = arr[index]
    if best < cur_sum:
        best = cur_sum
    prev = cur_sum

print(best)
