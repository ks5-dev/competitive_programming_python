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
    while(True):
        i = inp()
        if i == 42:
            break
        print(i)
main()
