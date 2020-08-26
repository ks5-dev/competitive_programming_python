def main():
    ans = 0
    a = int(input())
    inp = list(map(int,input().split()))
    for i in set(inp):
        p = inp.count(i)
        if p%2==0:
            ans+= p//2
        else:
            ans += (p-1)//2
    print(ans)
main()
