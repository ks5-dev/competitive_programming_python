from math import sqrt
def divisors(num):
    div = [1]
    for i in range (2,int(sqrt(num)+1)):
        if num%i == 0:
            div.append(i)
            if num/i != i:
                div.append(int(num/i))
    return div
def buddy(start,limit):
    for n in range(start,limit+1):
        m = sum(divisors(n)) - 1
        if sum(divisors(m)) - 1 == n and m > n:
            return [n,m]
            break
    return "Nothing"
print(sum(divisors(48)))
print(sum(divisors(75)))
print(buddy(10,50))