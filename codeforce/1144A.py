import sys
import string

def checkDup(seq):
    return len(seq) == len(set(seq))
def checkConsecutive(l):
    return sorted(l) == list(range(min(l), max(l)+1))

def main():
    for _ in range(int(input())):
        s = input()
        diverse =[string.ascii_lowercase.index(i) for i in s]
        if not checkDup(s):
            print("NO")
        else:
            if checkConsecutive(diverse):
                print("YES")
            else:
                print("NO")
main()
