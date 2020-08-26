def main():
    cnt = 0
    inp = set(map(int,input().split()))
    n = int(input())
    for _ in range(n):
        a = set(map(int,input().split()))
        if a < inp:
            cnt += 1
    print(cnt==n)
main()
