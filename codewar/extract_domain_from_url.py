from urllib.parse import urlparse

def find(url):
    res = urlparse(url)
    if res[1]:
        res = res[1].split('.')
    else:
        res = res[2].split('.')
    if "www" in res:
        return res[1]
    else:
        return res[0]

print(find("http://www.zombie-bites.com"))
print(find("http://github.com/carbonfive/raygun"))
print(find("www.xakep.ru"))
