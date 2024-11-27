import hashlib

def get_md5(password):
    md = hashlib.md5()
    md.update(b'Huanhuan.111')  # 加盐
    md.update(password.encode('utf-8'))
    res_md5_pas = md.hexdigest()
    return res_md5_pas

def auth_login(func):
    def inner(*args,**kwargs):
        from core import src
        if src.user_info['user_state']:
            res = func(*args,**kwargs)
            return res
        else:
            print('你没有登陆请先登陆!')
            src.login()
    return inner