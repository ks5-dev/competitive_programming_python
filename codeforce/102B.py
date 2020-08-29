import sys
input = sys.stdin.readline

def inp():
    return int(input())
def minp():
    return map(int,input().split())
def inpsl():
    return list(input().split())
def write(s):
    sys.stdout.write(s+" ")

def main():
    n = inp()
    cnt = 0
    while(n>9):
        n = sum([int(i) for i in str(n)])
        cnt += 1
    print(cnt)

main()
