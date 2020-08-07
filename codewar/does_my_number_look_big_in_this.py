def narcissistic(n):
    num = [int(i) for i in str(n)]
    sum = 0
    for i in num:
        sum += pow(i,len(num))
    return sum == n
