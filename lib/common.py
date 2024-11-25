import hashlib

def get_md5(password):
    md = hashlib.md5()
    md.update(b'Huanhuan.111')  # 加盐
    md.update(password.encode('utf-8'))
    res_md5_pas = md.hexdigest()
    return res_md5_pas