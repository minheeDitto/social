from ins.ins_login import get_cookies


cookies = []
item = {}
item["460020889@qq.com"] = 'siguma777x'
item["AnQistronger"] = 'zhanganqi666'
for key,value in item.items():
    cookies.append(get_cookies(key,value))

