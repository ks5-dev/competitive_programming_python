from math import sqrt,floor
def main():
    ans = 0
    inp = int(input())
    for i in range(floor(sqrt(inp))):
        j = i +1
        while(i*j <= inp):
            ans += 1
            j+=1
    print(ans)
main()
