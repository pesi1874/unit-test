#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class A:

    def __init__(self):
        self.name = 'a'
        self.get_name()

    def get_name(self):
        print(self.name)


class B(A):

    def get_name(self):
        self.name = 'b'
        super().get_name()


b = B()
