#!/usr/bin/python
#-*- coding:utf-8 -*-

from __future__ import division


def jia(x, y):
    return x + y


def jian(x, y):
    return x - y


def cheng(x, y):
    return x * y


def chu(x, y):
    return x / y


operator={"+":jia,"-":jian,"*":jia,"/":jia}

def f(x,o,y):
    print operator.get(o)(x,y)

f(3,"/",2)

def operator(x, o, y):
    if o == "+":
        print jia(x, y)
    elif o == "-":
        print jian(x, y)
    elif o == "*":
        print cheng(x, y)
    elif o == "/":
        print chu(x, y)
    else:
        pass

