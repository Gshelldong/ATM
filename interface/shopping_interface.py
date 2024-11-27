from db import db_handler
from interface import bank_interface


def goods_list():
    goods_dic = db_handler.goods_select()
    return goods_dic


def pay_shpping_car(user, cost):
    res = bank_interface.pay_interface(user,cost)
    if res:
        return True, f'{user}购买购物车商品付款{cost}成功！'
    return False,f'{user}购买购物车商品付款{cost}失败！'

def add_shopp_car(user, shopping_goods):
    user_dic = db_handler.select(user)
    shopp_car = user_dic.get('shopp_car')
    for goods in shopping_goods:
        # 如果购物车有相同的商品久把原来的数量+新增的数量
        if goods in shopp_car:
            car_goods_num = shopp_car[goods]
            shopp_car[goods] = car_goods_num + shopping_goods[goods]
        else:
            shopp_car[goods] = shopping_goods[goods]
    # 更新修改后的值
    user_dic['shopp_car'] = shopp_car
    db_handler.save(user_dic)
    return True, f'{user}添加购物车成功!'


def check_shopp_car(user):
    user_dic = db_handler.select(user)
    shopp_car = user_dic.get('shopp_car')
    return shopp_car
