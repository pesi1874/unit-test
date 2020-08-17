#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Foo(object):
    def __init(self, x, y=0):
        self.x = x
        self.y = y


def f():
    pass

f = Foo()
print(Foo.__class__)
print(type(Foo()))
print(type.__class__)
print(object.__class__)