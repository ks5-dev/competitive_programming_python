# O(n^2) time complexity
def max_sum(seq):
    result = 0
    a = 0
    while a< len(seq):
        sum = 0
        b = a
        while b<len(seq):
            sum+= seq[b]
            result = max(result,sum)
            b += 1
        a+=1
    return result

print(max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
