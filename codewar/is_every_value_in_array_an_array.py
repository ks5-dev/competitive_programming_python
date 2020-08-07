def arr_check(arr):
    c = 0
    for i in arr:
        if isinstance(i,list):
            c += 1
    return c==len(arr)
