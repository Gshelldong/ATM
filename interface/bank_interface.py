from db import db_handler

def withdraw_interface(user,draw_cash):
    user_dic = db_handler.select(user)
    if draw_cash.isdigit():
        draw_cash = abs(int(draw_cash))
        if user_dic['balance'] >= draw_cash:
            user_dic['balance'] -= draw_cash
            msg = f'用户{user}提现{draw_cash}成功!'
            user_dic['flow'].append(msg)
            db_handler.save(user_dic)
            return True, msg
    return False, '提现失败请重试!'

def pay_interface(user,cost):
    user_dic = db_handler.select(user)
    if user_dic['balance'] >= cost:
        user_dic['balance'] -= cost
        user_dic['flow'].append(f'{user}付款{cost}成功!')
        db_handler.save(user_dic)
        return True
    return False


def check_flow_interface(user):
    user_dic = db_handler.select(user)
    flow = user_dic.get('flow')
    if flow:
        return flow


def re_pay_interface(user,cash):
    user_dic = db_handler.select(user)
    user_dic['balance'] += cash
    msg = f'{user}还款{cash}成功!'
    user_dic['flow'].append(msg)
    db_handler.save(user_dic)
    return True,msg