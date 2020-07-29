import sys
input = sys.stdin.readline
def inp():
    return(int(input()))
t = inp()
results = []
while (t>0):
    a,k = input().split()
    a=int(a)
    k=int(k)
    while(k>1):
        a += min(int(i) for i in str(a)) * max(int(i) for i in str(a))
        k -= 1
    results.append(a)
    t -= 1

for result in results:
    print(result)
