import sys
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
    n = inp()
    p1 = set(linp()[1:])
    p2 = set(linp()[1:])
    l = [i for i in range(1,n+1)]
    for i in p1:
        if i in l:
            l.remove(i)
    for i in p2 :
        if i in l:
            l.remove(i)
    if len(l) != 0:
        print("Oh, my keyboard!")
    else:
        print("I become the guy.")
main()
