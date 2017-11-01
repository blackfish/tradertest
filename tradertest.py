# Orko Sarkar
# Trader Test
# tests mental addition, multiplication, square root estimation, and previous
# answer recall to help prepare for interviews
# Will repeat questions until correct answer except for recall.
# Sqrt estimation assumes user is using linear approximation.

import os
import math as m
import random
from decimal import Decimal,DecimalException

lasttwo = [] #stores the last two integers for recall
rand = -1 #
twoint = 0
while True:
# stops repeat recall questions
    if rand >= .8:
        while rand >= .8:
            rand = random.random()
    else:
        rand = random.random()
# addition
    if rand < .3:
# generate random numbers and sum
        a,b = random.randint(1,100),random.randint(1,100)
        c = a+b
        sol = -1
# test sum
        while sol != c:
            print(str(a) + '+' + str(b))
            os.system('sleep 5')
            os.system('clear')
# catch input errors
            while True:
                try:
                    sol = int(input('solution:\n'))
                    os.system('clear')
                    break
                except ValueError:
                    os.system('clear')
                    print('Invalid input, try again.')
        lasttwo.append(sol)
        print('Correct!')
        twoint = twoint + 1
# multiplication
    elif rand < .6:
# generate random numbers and product
        a,b = random.randint(1,50),random.randint(1,50)
        c = a*b
        sol = -1
# test product
        while sol != c:
            print(str(a) + '*' + str(b))
            os.system('sleep 5')
            os.system('clear')
# catch input errors
            while True:
                try:
                    sol = int(input('solution:\n'))
                    os.system('clear')
                    break
                except ValueError:
                    os.system('clear')
                    print('Invalid input, try again.')
        lasttwo.append(sol)
        print('Correct!')
        twoint = twoint + 1 
# square root estimation
    elif rand < .75:
# generate random number, squareroot, and linear approximation
        a = random.randint(1,100)
        c = m.sqrt(a)
        upper = m.ceil(c)**2
        lower = m.floor(c)**2
        while (upper - lower)==0:
            a = random.randint(1,100)
            c = m.sqrt(a)
            upper = m.ceil(c)**2
            lower = m.floor(c)**2
        est = Decimal(m.floor(c) + (a-lower)/(upper-lower))
        sol = -1
# test square root
# since linear approximation will always be under sqrt, truncate at 2 decimal
# places and use that as the lower bound - should never estimate over
        while sol < m.floor(est*100)/100 or sol > c:
            print('square root of ' + str(a))
            os.system('sleep 5')
            os.system('clear')
# catch input errors
            while True:
                try:
                    sol = Decimal(float(input('solution:\n')))
                    os.system('clear')
                    break
                except (ValueError, DecimalException):
                    os.system('clear')
                    print('Invalid input, try again.')
        print('Correct!')
        twoint = 0
# recall last integer
    elif len(lasttwo) == 2 and twoint > 1: 
# test last integer, and catch input errors
        while True:
            try:
                if int(input('What was the solution before the last \n')) == lasttwo[0]:
                    os.system('clear')
                    print('Correct!')
                    break
                else:
                    print('Incorrect, correct answer is ' + str(lasttwo[0]))
                    os.system('sleep 5') 
                    os.system('clear')
                    break
                break
            except ValueError:
                    os.system('clear')
                    print('Invalid input, try again.')
        twoint = 0
    if len(lasttwo) == 3:
        lasttwo.pop(0)
