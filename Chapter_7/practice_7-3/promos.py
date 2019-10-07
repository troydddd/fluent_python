# -*- coding: utf-8 -*-

# 使用装饰器来存储每个promo strategy，省去了先创建一个空list
# 然后往list里一个一个地装promo strategy的步骤

promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity(order):
    """为积分为1000以上的顾客提供5%折扣"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


@promotion
def large_order(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0

@promotion
def bulk_item(order):
    """单个商品为20个以上时提供10%折扣"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


def best_promo(order):
    """选择可用的最佳折扣"""
    return max(promo(order) for promo in promos)
