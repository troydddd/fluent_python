# -*- coding: utf-8 -*-

import time
from clock import clock

@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)


if __name__ == '__main__':
    snooze(.123)
    factorial(10)