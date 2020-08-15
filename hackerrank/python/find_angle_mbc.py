import math
def find_mbc():
    ab = int(input())
    bc = int(input())
    mbc = math.degrees(math.atan(ab/bc))
    print(str(int(round(mbc)))+"°")

find_mbc()
