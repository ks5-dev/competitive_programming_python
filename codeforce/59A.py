def main():
    s = input()
    cnt_u = cnt_l = 0
    for i in s:
        if i.isupper():
            cnt_u += 1
        else:
            cnt_l += 1
    if(cnt_l >= cnt_u):
        print(s.lower())
    else:
        print(s.upper())
main()
