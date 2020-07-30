#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Animal:
    def __init__(self, Animal):
        print(Animal, 'is an animal.')


class Mammal(Animal):
    def __init__(self, mammalName):
        print(mammalName, 'is a warm-blooded animal.')
        super().__init__(mammalName)


class NonWingedMammal(Mammal):
    def __init__(self, NonWingedMammal):
        print(NonWingedMammal, "can't fly.")
        super().__init__(NonWingedMammal)


class NonMarineMammal(Mammal):
    def __init__(self, NonMarineMammal):
        print(NonMarineMammal, "can't swim.")
        super().__init__(NonMarineMammal)


class Dog(NonMarineMammal, NonWingedMammal):
    def __init__(self):
        print('Dog has 4 legs.')
        super().__init__('Dog')


# d = Dog()
# print('')
# bat = NonMarineMammal('Bat')

# 查看继承顺序
# print(Dog.__mro__)


class Base:
    def __init__(self):
        print('base')

    def t(self):
        print(1)

class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent, Base):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类 FooChild 的对象转换为类 FooParent 的对象
        super(FooChild).__init__()
        print('Child')

    # def bar(self, message):
    #     super(FooChild, self).bar(message)
    #     print('Child bar fuction')
    #     print(self.parent)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar('HelloWorld')
    fooChild.t()
