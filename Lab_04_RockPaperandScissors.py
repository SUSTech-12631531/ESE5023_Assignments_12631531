# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:03:07 2026

@author: Administrator
"""

import random

#电脑随机选取一个key
choice = {"rock" : 1, "paper" : 2, "scissors" : 3}
computer_choice = random.choice(list(choice.keys()))

#人为输入一个key
your_choice = input("Enter rock, paper, or scissors: ")

#分别输出电脑和人的选择
print("computer choice", computer_choice)
print("your choice", your_choice)

#将电脑和人选的key转换为对应的val
computer_val = choice[computer_choice]
your_val = choice[your_choice]

#得出两个val差的绝对值
diff = abs(computer_val - your_val)

#对val差的绝对值进行判断
if diff == 1:
   winner = max(computer_val, your_val)
   if winner == computer_val:
       print("You Lose...") 
   else:
       print("You Win!!")
elif diff == 2:
    winner = min(computer_val, your_val)
    if winner == computer_val:
        print("You Lose...") 
    else:
        print("You Win!!")
else:
    print("Draw")


