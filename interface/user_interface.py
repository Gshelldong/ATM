from db import db_handler
from lib import common

def check_user_interface(user):
    user_dic = db_handler.select(user)
    if user_dic:
        return True

def register_interface(username,password):
    salt_md5_pas = common.get_md5(password)
    user_dit = {
        'username': username,
        'password': salt_md5_pas
    }

    db_handler.save(user_dit)

    return  f'{user_dit.get("username")}用户注册成功!'