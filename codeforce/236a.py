def main():
    tmp = []
    str_input = input()
    for s in str_input:
        tmp.append(s)
    tmp = set(tmp)
    if len(tmp) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

main()
