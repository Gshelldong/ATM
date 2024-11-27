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