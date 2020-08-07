def countbit(n):
    tmp = bin(n)
    return sum([int(i) for i in tmp if i.isdigit() and int(i)==1])
