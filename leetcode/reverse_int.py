import sys
def reverse(n):
    result= 0
    if n > 0:
        result =  int(str(n)[::-1])
    else :
        result = 0 - (int(str(0-n)[::-1]))
    if result >= 2** 31 -1 or result <= -2** 31 :
        result = 0
    return result

print(reverse(1534236469))
