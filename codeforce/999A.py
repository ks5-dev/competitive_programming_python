def main():
    n,k = map(int,input().split())
    problems = list(map(int,input().split()))
    while(len(problems) != 0):
        if k >= problems[0] :
            problems.pop(0)
        elif k >= problems[-1]:
            problems.pop()
        else:
            break
    print(n-len(problems))

main()
