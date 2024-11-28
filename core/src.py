from interface import user_interface,bank_interface,shopping_interface
from lib import common

user_info = {
    'user_state': None
}

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
        flag,msg = user_interface.check_user_interface(username)
        if not flag:
            if count ==1:
                print("尝试用户名最大次数！")
                break
            print(msg)
            count -=1
            continue

        password = input('请输入用户名密码>>>: ')
        # 调用密码校验的接口
        res,msg = user_interface.login_interface(username,password)
        if res:
            print(msg)
            user_info['user_state'] = username
            break
        print(msg)

@common.auth_login
# 查看余额
def check_bal():
    bal = user_interface.check_bal_interface(user_info['user_state'])
    print(bal)

# 提现
@common.auth_login
def withdraw():
    print("你现在使用提现功能!")
    draw_cash = input('请输入你想提现多少>>>: ').strip()
    flag,msg = bank_interface.withdraw_interface(user_info['user_state'],draw_cash)
    if not flag:
        print(msg)
    print(msg)

def repay():
    while True:
        cash = input('')
    bank_interface.re_pay_interface(user_info['user_state'],cash)

# 转账
@common.auth_login
def transfer():
    count = 0
    while count < 3:
        to_user = input('请输入你想转账的用户>>>: ')
        res = user_interface.check_user_interface(to_user)
        if not res:
            count +=1
            if count == 3:
                print('尝试最大次数推出!')
                break
            print('该用户不存在请重新输入！')
            continue
        money = input('请输入你想转账的金额>>>: ').strip()
        if money.isdigit():
            money = int(money)
            flag, msg = bank_interface.transfer_interface(user_info['user_state'], to_user, money)
            if flag:
                print(msg)
                break
            print(msg)
            break

@common.auth_login
def check_flow():
    res_flow = bank_interface.check_flow_interface(user_info['user_state'])
    if res_flow:
        for flow in res_flow:
            print(flow)
    else:
        print('你还没有流水!')

def shop_car():
    # 查询现有的商品列表
    goods_dic = shopping_interface.goods_list()
    # 商品的菜单索引
    goods_index = {}
    # cost 只是一个展示
    cost = 0
    shopping_goods = {}
    while True:
        print('输入q退出购物车.')
        for i, j in enumerate(goods_dic, 1):
            print('%s: %s - ￥%s' % (i, j.center(10), goods_dic[j]))
            goods_index[i]=j
            goods_index[i]=j
        choice = input('请选择你想要购买的商品>>>: ').strip()
        if choice.isdigit():
            choice = int(choice)
            if choice >=1 and choice <= len(goods_dic):
                goods = goods_index[choice]
                goods_price = goods_dic[goods]
                print('你放了一件%s商品到购物车,金额: %s元. %s + 1'%(goods,goods_price,goods))
                if shopping_goods.get(goods):
                    shopping_goods[goods] += 1
                else:
                    shopping_goods[goods] = 1
                cost += goods_price
                print('你现在购物车共计%s元.'%cost)
            else:
                print('请输入正确的商品编号!')
        if choice == 'q':
            choice_pay = input('是否付款Y/N: ').strip()
            choice_pay = choice_pay.lower()
            if choice_pay == 'y':
                res,msg = shopping_interface.pay_shpping_car(user_info['user_state'],cost)
                if res:
                    # 购买成功后把购物车清空
                    print(msg)
                    goods_index.clear()
                    break
                else:
                    print(msg)
            elif choice_pay == 'n':
                shopping_interface.add_shopp_car(user_info['user_state'],
                                                 shopping_goods)
                break
            else:
                print('余额不足请充值!')
                # 余额不足

@common.auth_login
def check_shopping_car():
    shopp_car = shopping_interface.check_shopp_car(user_info['user_state'])
    if not shopp_car:
        print("你的购物车是空的!")
    print(shopp_car)

def login_out():
    flag,msg = user_interface.login_out_interface(user_info['user_state'])
    if flag:
        print(msg)


def lock_user():
    user = input('请输入你想锁定的用户>>>: ')
    flag,msg = user_interface.lock_user_interface(user)
    if flag:
        print(msg)
    else:
        print(msg)

def unlock_user():
    user = input('请输入你想解锁的用户>>>: ')
    flag,msg = user_interface.unlock_user_interface(user)
    if flag:
        print(msg)
    else:
        print(msg)
def add_user():
    pass

def change_balance():
    pass

@common.auth_login
def admin_manage():
    admin_menu = {
        '1': add_user,
        '2': lock_user,
        '3': unlock_user,
        '4': change_balance
    }

    while True:
        if user_info['user_state'] != 'admin':
            print('你不是管理员，无法使用此功能！')
            break
        print("""
            1 -> 添加用户
            2 -> 锁定用户
            3 -> 解锁用户
            4 -> 修改用户余额
            按q退出
        """)
        choice = input('请输入想要得功能编号>>>: ')
        if choice == 'q':
            break
        if choice in admin_menu:
            admin_menu[choice]()
        else:
            print("请输入正确得功能编号!")
            break




action_menu = {
    '1': register,
    '2': login,
    '3': check_bal,
    '4': withdraw,
    '5': repay,
    '6': transfer,
    '7': check_flow,
    '8': shop_car,
    '9': check_shopping_car,
    '10': login_out,
    '11': admin_manage
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
            8 -> 购物车
            9 -> 查看购物车
            10 -> 注销
            11 -> 管理员功能
        """)
        choice = input('请输入想操作的功能>>>: ').strip()
        if choice not in action_menu:
            print('请输入正确的编号!')
            continue
        action_menu[choice]()



