from db import db_handler
from lib import common

def check_user_interface(user):
    user_dic = db_handler.select(user)
    if user_dic:
        return True

def register_interface(username,password,blance=15000):
    salt_md5_pas = common.get_md5(password)
    # 把用户的信息保存在一个字典里面
    user_dit = {
        'username': username,
        'password': salt_md5_pas,
        'balance': blance,
        'flow': [],
        'shopp_car': {},
        'lock': False
    }

    db_handler.save(user_dit)

    return  f'{user_dit.get("username")}用户注册成功!'

def login_interface(user,password):
    user_dic = db_handler.select(user)
    password = common.get_md5(password)

    if password == user_dic.get('password'):
        return True,f'用户{user}登陆成功!'
    return False,f'用户{user}登陆失败!'

def check_bal_interface(username):
    user_dic = db_handler.select(username)
    return user_dic.get('balance')

