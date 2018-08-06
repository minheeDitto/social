from html.parser import HTMLParser
# a = '&#xe15;&#xe27;&#xe31;&#xe19;&#xe2a;&#xe32;&#xe22; &#xe2a;&#xe38;&#xe14;&#xe2a;&#xe32;&#xe22;&#xe1b;&#xe48;&#xe32;&#xe19;'
# b = 'aaa'
# html = HTMLParser()
# txt = html.unescape(a)
# print(txt)
# import time
# print(time.time())
# print(HTMLParser().unescape('https\\3a \/\/scontent-lax3-1.xx.fbcdn.net\/v\/t1.0-9\/fr\/cp0\/e15\/q65\/37387913_372931406570120_2408557362550931456_n.jpg?_nc_cat\\3d 0\\26 efg\\3d eyJpIjoidCJ9\\26 oh\\3d fe2b105f1b3b75ceee4efc0bf2f402d8\\26 oe\\3d 5BD531B5'))
a = '\\u0e2d\\u0e22\\u0e32\\u0e01\\u0e2b\\u0e25\\u0e07\\u0e23\\u0e31\\u0e01 \\u0e16\\u0e49\\u0e32\\u0e44\\u0e21\\u0e48\\u0e02\\u0e31\\u0e14\\u0e43\\u0e08'
print(eval("u\"" + a + "\""))

