# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/python
def convert_str(str):
    str = str.lower()
    result = ""
    for i in str:
        if str.count(i) != 1:
            result += ")"
        else:
            result += "("
    return result
