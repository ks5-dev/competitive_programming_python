def is_leap(year):
    if year%4 == 0 :
        if year %100 == 0:
            if year%400 != 0:
                return False
            else:
                return True
        else:
            return True


year =int(input())
is_leap(year)
