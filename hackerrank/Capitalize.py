import sys
def main():
    s = list(input().split())
    for i in s:
        sys.stdout.write(i[0].upper()+i[1:]+" ")
main()
