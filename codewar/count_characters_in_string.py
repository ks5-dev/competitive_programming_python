#https://www.codewars.com/kata/52efefcbcdf57161d4000091/python
def count_char(str):
    dictionary = {}
    list_char = []
    list_num = []
    for i in set(str):
        list_char.append(i)
        list_num.append(str.count(i))
    dictionary = dict(zip(list_char, list_num))
    return dictionary
