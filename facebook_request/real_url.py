import re
def change(url):
    if '\\3d' in url:
        first = re.sub(r'\\3d ', '=', url)
        second = re.sub(r'\\26 ','&', first)
        third = re.sub(r'\\3a ', ':', second)
        real = re.sub(r'\\','',third)
        return real



def change_code(text):
    return text.encode().decode()