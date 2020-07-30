#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 类调用写法
# class A:
#     def __init__(self):
#         self.a = 1
#         B(self).test()
#
# class B:
#     def __init__(self, app):
#         self.name = app.a
#
#     def test(self):
#         print(self.name)
#
# a = A()


import sys
import os


def getcwd():
    # get current path, try to use PWD env first
    try:
        a = os.stat(os.environ['PWD'])
        b = os.stat(os.getcwd())
        if a.st_ino == b.st_ino and a.st_dev == b.st_dev:
            cwd = os.environ['PWD']
        else:
            cwd = os.getcwd()
    except:
        cwd = os.getcwd()
    return cwd


# print(sys.argv[:])
# print(sys.executable)
print(getcwd())
