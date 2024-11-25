import os
from conf import settings
import json

def save(user_dit):
    # 把用户信息写入文件中
    user_path = os.path.join(settings.DB_DIR, f'{user_dit["username"]}.json')
    with open(user_path, mode='w', encoding='utf-8') as f:
        dumps_user_dit = json.dump(user_dit, f)
        f.close()

def select(user):
    user_path = os.path.join(settings.DB_DIR, f'{user}.json')
    if os.path.exists(user_path):
        # 存在就读取里面的内容
        with open(user_path,mode='r',encoding='utf-8') as f:
            res_user_dic = json.load(f)
            return res_user_dic
        f.close()