
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
print('We will ask for your name and run some things with it to ensure the program you are running this in is configured correctly.')
print('What is your name?')
name = input()
time.sleep(0.5)
loop = True
ans = 'T'
while loop == True:
    if len(ans) <= 1:
    	print('Hello ' + name + '. Please verify that this if your name.')
    	print('Answer yes or no.')
    	ans = str(input())
    	ans = ans.lower()
    else:
    	print('Your real name is ' + name + ', right?')
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
        print('        Why is a pineapple pen not an apple pen?         ')
        print('*********************************************************')
        print('                  Choose A, B, C, or D                   ')
        print('*********************************************************')
        print('Option A: Beucause                                       ')
        print('*********************************************************')
        print('Option B: Cheese')
        print('*********************************************************')
        print('Option C: Cracker')
        print('*********************************************************')
        print('Option D: Butter')
        print('*********************************************************')
        ans = str(input())
        ans = ans.lower()
        rans = str('c')
        if ans == rans:
        	print('Good Job, ' + name + '. You got it right. Do you understand why?')
        	print('Answer yes or no')
        	why = str(input())
        	why = why.lower()
        	if why == 'no':
        		print('Explanation')
        	time.sleep(0.5)
        	print('checkpoint')
        elif ans == 'a':
        	print('Answer A is incorrect, ' + name + '.')
        break
    elif ans == 'no':
        print('What is your name actually?')
        name = str(input())

        continue

    else:
        print('Please answer with yes or no. ' + ans + ' is not yes or no.')
        time.sleep(0.5)
        continue
