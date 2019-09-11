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


