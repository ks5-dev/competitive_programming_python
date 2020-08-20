def main():
    for i in range(int(input())):
        n = int(input())
        result = 1
        for i in range(2,n+1):
            result *= i
        print(result)

main()
