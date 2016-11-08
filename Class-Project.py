import subprocess
import json
import os
import itertools
import time
import random

# 'Contains' function, Created by Adrian Hall. https://github.com/aderhall
def contains(origin, text):
    vf = False
    soc = 0
    i = -1
    loop = True
    while loop:
        vf = False
        i += 1
        if origin[i] == text[0]:
            a = -1
            loop2 = True
            while loop2:
                a += 1
                try:
                    if origin[a+i] != text[a]:
                        vf = True
                except:
                    vf = True
                if a >= (len(text)-1):
                    loop2 = False
        else:
            vf = True
        if vf == False:
            soc += 1
        if i >= (len(origin)-1):
            loop = False
            vf = True
    return soc


print('Welcome to Michael Turner, Jake Leach, and Tobias Ward\'s MYP project.')
time.sleep(0.5)
print('This is an interactive game/quiz that will both quiz you, and teach you about three parts of history.')
time.sleep(2)
print('We will ask for your name and run some things with it to ensure the program you are running this in is configured correctly.')
print('What is your name?')
name = raw_input()
time.sleep(0.5)
loop = True
ans = 'T'
q1 = True
q2 = True
q3 = True
q4 = True
A = True
B = True
C = True
D = True
Alpha = False
Beta = False
Charlie = False
Delta = False

while loop == True:
    if len(ans) <= 1:
    	print('Hello ' + name + '. Please verify that this if your name.')
    	print('Answer yes or no.')
    	ans = raw_input('')
    	ans = ans.lower()
    else:
    	print('Your real name is ' + name + ', right?')
    	print('Answer yes or no.')
    	ans = raw_input('')
    	ans = ans.lower()
    A = True
    B = True
    C = True
    D = True
    if ans == 'yes':
        while q1 == True:
            print('*********************************************************')
            print('                         Part: 1                         ')
            print('*********************************************************')
            print('               Renaissance and Reformation               ')
            print('*********************************************************')
            time.sleep(2)
            print()
            print()
            print('*********************************************************')
            print('                      Question: 1                        ')
            print('*********************************************************')
            print('        Why is a pineapple pen not an apple pen?         ')
            print('*********************************************************')
            print('                  Choose A, B, C, or D                   ')
            print('*********************************************************')
            time.sleep(2)
            if A == True:
                print('Option A: Because')
                print('*********************************************************')
                time.sleep(0.5)
            if B == True:
                print('Option B: Cheese')
                print('*********************************************************')
                time.sleep(0.5)
            if C == True:
                print('Option C: Cracker')
                print('*********************************************************')
                time.sleep(0.5)
            if D == True:
                print('Option D: Butter')
                print('*********************************************************')
                time.sleep(0.5)
            ans = raw_input('')
            ans = ans.lower()
            rans = str('b')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why?')
                q1 = False
                print('Answer yes or no')
                why = raw_input('')
                why = why.lower()
                if why == 'no':
                    print('Explanation')
                    time.sleep(0.5)
                    print('checkpoint')
                    break


            elif ans == 'a':
                print('Answer A is incorrect, ' + name + '.')
                print('Correction text')
                A = False
                continue
            elif ans == 'c':
                print('Answer C is incorrect, ' + name + '.')
                print('Correction text')
                B = False
                continue
            elif ans == 'd':
                print('Answer D is incorrect, ' + name + '.')
                print('correction text')
                D = False
                continue
            else:
                print('\'' + ans + '\' is not an option.')
        A = True
        B = True
        C = True
        D = True
        while q2 == True:
            print('*********************************************************')
            print('                      Question: 2                        ')
            print('*********************************************************')
            print('        Why is a pineapple pen not an apple pen?         ')
            print('*********************************************************')
            print('                     Choose A or B                       ')
            print('*********************************************************')
            if A == True:
                print('Option A: True')
                print('*********************************************************')
            if B == True:
                print('Option B: False')
                print('*********************************************************')
            ans = raw_input()
            ans = ans.lower()
            rans = str('a')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why?')
                q1 = False
                print('Answer yes or no')
                why = raw_input('')
                why = why.lower()
                if why == 'no':
                    print('Explanation')
                    time.sleep(0.5)
                    print('checkpoint')
                    break
                if why == 'yes':
                    print('Next Question')
                    time.sleep(2)
                    break
            elif ans == 'b':
                print('Answer B is incorrect, ' + name + '.')
                print('Correction text')
                B = False
                continue
            else:
                print(ans + ' is not A or B')
                continue
        A = True
        B = True
        C = True
        D = True
        while q3 == True:
            print('*********************************************************')
            print('                      Question: 2                        ')
            print('*********************************************************')
            print('        Why is a pineapple pen not an apple pen?         ')
            print('*********************************************************')
            print('    Answer with a short answer. Your response will be    ')
            print('         checked with keywords.          ')
            print('*********************************************************')
            ans = raw_input('')
            ans = ans.lower()
            if contains(ans, 'i ') >= 1:
                Alpha = True
                print('A')
            if contains(ans, 'am') >= 1:
                Beta = True
                print('B')
            if contains(ans, 'a') >= 1:
                Charlie = True
                print('C')
            if contains(ans, 'tate') >= 1:
                Delta = True
                print('D')
            if Alpha == True and Beta == True and Charlie == True and Delta == True:
                print('Success')



            break




        break

    elif ans == 'no':
        print('What is your name actually?')
        name = raw_input('')

        continue

    else:
        print('Please answer with yes or no. ' + ans + ' is not yes or no.')
        time.sleep(0.5)
        continue
