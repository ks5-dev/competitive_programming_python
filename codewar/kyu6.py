#Multiples of 3 or 5

def findSum(n):
    return sum([i for i in range(n) if i%5==0 or i%3==0])

#Difference of 2
def twos_difference(lst):
    # your code here
    result = []
    arr = sorted(lst)
    for i in arr :
        for j in arr :
            if i == j-2:
                result.append((i,j))
    return result

#Bit Counting
def countbit(n):
    tmp = bin(n)
    return sum([int(i) for i in tmp if i.isdigit() and int(i)==1])

#Find the odd int
def find_it(seq):
    for i in range(len(seq)):
        count = 0
        for j in range(len(seq)):
            if seq[i] == seq[j]:
                count+=1

        if (count % 2 != 0):
            return seq[i] 
