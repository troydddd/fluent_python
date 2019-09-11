# -*- coding: utf-8 -*-

def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

if __name__ == '__main__':
    target()
    target