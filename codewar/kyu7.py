#Nth Smallest Element (Array Series #4)
def find_n(arr,i):
    return sorted(arr)[i-1]

#Is every value in the array an array?
def arr_check(arr):
    c = 0
    for i in arr:
        if isinstance(i,list):
            c += 1
    return c==len(arr)
