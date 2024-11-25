from interface import user_interface

def register():
    print('用户注册.')
    username = input('请输入用户名>>>: ').strip()

    # 判断用户名是否存在
    user_exits = user_interface.check_user_interface(username)
    if user_exits:
        print('用户已经存在，请重新注册用户!')

    password = input('请设置用户密码: ').strip()
    re_password = input('请确认用户密码: ').strip()

    # 正常注册
    if re_password == password:

        # 用户入库
        msg = user_interface.register_interface(username,password)
        if msg:
            print(msg)
        else:
            print('注册失败!')
    else:
        print('两次输入密码不一致.')


def login():
    count = 3
    while count:
        username = input('请输入用户名>>>: ')
        # 判断用户是否存在
        flag = user_interface.check_user_interface(username)
        if not flag:
            print("非法用户请重新输入！")
            count -=1
        password = input('请输入用户名密码>>>: ')
        # 调用密码校验的接口






# 查看余额
def check_bal():
    pass

# 提现
def withdraw():
    pass

def repay():
    pass

# 转账
def transfer():
    pass

def check_flow():
    pass

def check_shopping_car():
    pass

def login_out():
    exit(0)


action_menu = {
    '1': register,
    '2': login,
    '3': check_bal,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': check_shopping_car,
    '9': login_out
}

def run():
    while True:
        print("""
            1 -> 注册
            2 -> 登陆
            3 -> 查看余额
            4 -> 提现
            5 -> 还款
            6 -> 转账
            7 -> 查看流水
            8 -> 查看购物车
            9 -> 注销
        """)
        choice = input('请输入想操作的功能>>>: ').strip()
        if choice not in action_menu:
            print('请输入正确的编号!')
            exit(1)
        action_menu[choice]()

