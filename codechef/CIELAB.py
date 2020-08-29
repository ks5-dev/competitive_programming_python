import sys
input = sys.stdin.readline

def inp():
    return int(input())
def minp():
    return map(int,input().split())
def linp():
    return list((int,input().split()))
def inpsl():
    return list(input().split())
def write(s):
    sys.stdout.write(s+" ")

def main():
    a,b = minp()
    c = a-b
    if(c%10 == 0):
        print(c+1)
    else:
        print(c-1)
main()
