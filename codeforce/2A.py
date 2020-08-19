from collections import defaultdict
def main():
    dict = defaultdict()
    for i in range(int(input())):
        name,score = input().split()
        score = int(score)
        dict[name] += score
    print(dict)
    print(max(dict, key = dict.get))

main()
