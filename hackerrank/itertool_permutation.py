# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

def main():
    s,n = input().split()
    n = int(n)
    result = sorted(["".join(i) for i in permutations(s,n)])
    for r in result :
        print(r)
main()
