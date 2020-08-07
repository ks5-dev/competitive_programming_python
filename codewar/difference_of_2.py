def twos_difference(lst):
    # your code here
    result = []
    arr = sorted(lst)
    for i in arr :
        for j in arr :
            if i == j-2:
                result.append((i,j))
    return result
