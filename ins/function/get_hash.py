import hashlib

def gen_hash(*args):
    """
    合并任意个对象并生成MD5值
    :param args:
    :return: hash
    """
    mix = ''
    for arg in args:
        if arg:
            mix += str(arg)
    md5 = hashlib.md5()
    md5.update(mix.encode('utf-8'))
    return md5.hexdigest()