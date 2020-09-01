import sys
from itertools import product
sys_input = sys.stdin.readline

def inp():
    return int(sys_input())
def minp():
    return map(int,sys_input().split())
def linp():
    return list(map(int,sys_input().split()))
def inpsl():
    return list(input().split())
def write(s):
    sys.stdout.write(s+" ")

def main():
    op = [7,8]
    n = inp()
    s = 0
    for i in range(1,n+1):
        s += len((list(product(op,repeat = i))))
    print(s)
main()
