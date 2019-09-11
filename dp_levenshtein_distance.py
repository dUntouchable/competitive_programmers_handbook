#
# Levenshtein distance
# the minimum number of edit# ing operations needed to transform a string into another string. 
# The allowed # editing operations are as follows:
# • insert a character (e.g. ABC → ABCA )
# • remove a character (e.g. ABC → AC )
# • modify a character (e.g. ABC → ADC )
#

def min_edits(first, second):
    val_arr = [[0 for _ in range(len(second)+1)] for _ in range(len(first)+1)]
    for i in range(len(val_arr)):
        val_arr[i][0] = i
    for i in range(len(val_arr[0])):
        val_arr[0][i] = i
    #print(val_arr)

    for i in range(1,len(val_arr)):
        for j in range(1,len(val_arr[0])):
            if first[i-1] != second[j-1]:
                val_arr[i][j] = min(val_arr[i-1][j] + 1,
                                    val_arr[i][j-1] + 1,
                                    val_arr[i-1][j-1] + 1)
            else:
                val_arr[i][j] = min(val_arr[i - 1][j] + 1,
                                    val_arr[i][j - 1] + 1,
                                    val_arr[i - 1][j - 1])
    print(first, " ",second, " ", val_arr[-1][-1])

min_edits("LOVE", "MOVIE")
min_edits("FLOMAX", "VOLMAX")
min_edits("GILY", "GEELY")
min_edits("HONDA", "HYUNDAI")
