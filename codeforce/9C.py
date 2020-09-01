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
    cnt =0
    for i in range(1,2**10):
        if int(bin(i)[2:]) <= n:
            cnt += 1
        else:
            break
    print(cnt)

main()
