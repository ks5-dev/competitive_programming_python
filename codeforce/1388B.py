import math
import sys
def main():
    for i in range(int(input())):
        x = int(input())
        n = math.floor( (x+3)/4 )
        for j in range(x-n):
            sys.stdout.write(str(9))
        for k in range(n):
            sys.stdout.write(str(8));
        sys.stdout.write("\n")
main()
