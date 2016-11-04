
import asyncio
import subprocess
import json
import os
import itertools
import time
import random

# 'Contains' function, Created by Adrian Hall.
def contains(origin, text):
    print ('Text: ' + text)
    vf = False
    soc = 0
    i = -1
    loop = True
    while loop:
        vf = False
        i += 1
        print ('Testing letter:' + str(i) + ' (' + origin[i] + ')')
        if origin[i] == text[0]:
            a = -1
            loop2 = True
            while loop2:
                a += 1
                print ('Trying: ' + str(a) + ' ' + text[a])
                try:
                    if origin[a+i] != text[a]:
                        print ('Canceled search')
                        vf = True
                except:
                    vf = True
                if a >= (len(text)-1):
                    loop2 = False
        else:
            vf = True
        if vf == False:
            soc += 1
            print ('Found occurance')
        if i >= (len(origin)-1):
            loop = False
            vf = True
    print (soc)
    return soc


print('Welcome to Michael Turner, Jake Leach, and Tobias Ward\'s MYP project.')
time.sleep(0.5)
print('This is an interactive game/quiz that will both quiz you, and teach you about three parts of history.')
time.sleep(2)
print('What is your name?')
name = input()
time.sleep(0.5)
loop = True
while loop == True:
    print('Hello ' + name + '. Please verify that this if your name.')
    print('Answer yes or no.')
    ans = str(input())
    ans = ans.lower()

    if ans == 'yes':
        print('*********************************************************')
        print('                         Part: 1                         ')
        print('*********************************************************')
        print('               Renaissance and Reformation               ')
        print('*********************************************************')
        time.sleep(2)
        print()
        print()
        print('*********************************************************')
        print('                       Question:1                        ')
        print('*********************************************************')
        print('                  Choose A, B, C, or D                   ')
        print('*********************************************************')

        break
    elif ans == 'no':
        print('What is your name actually?')
        ans = str(input())
        ans = ans.lower()
        continue

    else:
        print('Please answer with yes or no. ' + ans + ' is not yes or no.')
