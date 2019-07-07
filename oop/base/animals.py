#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
多态
"""

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        """
        重写父类的方法
        :return:
        """
        print('Dog is running...')

    def eat(self):
        """
        自定义方法
        :return:
        """
        print('Eating meat...')

class Cat(Animal):
    pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
