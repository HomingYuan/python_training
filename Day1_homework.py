#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: Homing
@software: PyCharm Community Edition
@file: Day1_homework.py
@time: 2017/5/8 19:14
"""


import random


def guess_the_num(num):
    while True:
        a = int(input("Please enter a number:"))
        if a > num:
            print("The number is bigger:")
        elif a < num:
            print("The number is smaller")
        else:
            print("You are right!")
            break


def game_continue_exit():
    while True:
        str1 = input('enter yes continue and no to exit:')
        if str1 == 'no':
            print('Exit the game...')
            break
        if str1 == 'yes':
            print('Continue the game')
            num = random.randint(0, 99)
            guess_the_num(num)


def main():
    print("-------Begin game--------")
    num = random.randint(0, 99)
    guess_the_num(num)
    game_continue_exit()


if __name__ == "__main__":
    main()
