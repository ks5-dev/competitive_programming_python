def main():
    a,b,n=map(int,input().split())
    mon = a
    if(a%10==0 and b==10):
        a =str(a)
        a += "0"*n
        a = int(a)
        print(a)
    else:
        while n!=0:
            for i in range(10):
                if (a*10+i) %b == 0:
                    a = int(str(a)+str(i))
                    break
            if a==mon:
                print(-1)
                break
            n-=1
        print(a)
main()
