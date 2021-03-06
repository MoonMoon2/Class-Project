import subprocess
import json
import os
import itertools
import time
import random
from tkinter import*
import urllib
from urllib.request import urlopen
import base64

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
name = input()
time.sleep(0.5)
loop = True
ans = 'T'
q1 = True
q2 = True
q3 = True
q4 = True
q5 = True
q6 = True
q7 = True
q8 = True
q9 = True
q10 = True
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
    	ans = input('')
    	ans = ans.lower()
    else:
    	print('Your real name is ' + name + ', right?')
    	print('Answer yes or no.')
    	ans = input('')
    	ans = ans.lower()
    if ans == 'yes'|| ans == 'y':
        loop == False
        A = True
        B = True
        C = True
        D = True
        print('*********************************************************')
        print('                         Part: 1                         ')
        print('*********************************************************')
        print('               Renaissance and Reformation               ')
        print('*********************************************************')
        print('                     Gutenberg Bible                     ')
        print('*********************************************************')
        print('')
        print('')
        time.sleep(0.5)
        while q1 == True:
            root = Tk()
            URL = "http://3.bp.blogspot.com/-Y-VdIkzl1V8/UAAyo1PsJFI/AAAAAAAABQo/HEcCJ2uFT_Q/s1600/gbible.gif"
            a = urllib.request.urlopen(URL)
            RI = a.read()
            a.close()
            b = base64.encodestring(RI)
            image = PhotoImage(data=b)
            label = Label(image=image)
            label.pack()
            root.mainloop()
            time.sleep(2)
            print('')
            print('')
            print('*********************************************************')
            print('                      Question: 1                        ')
            print('*********************************************************')
            print('                   What is Secularism?                   ')
            print('*********************************************************')
            print('               Type \'A\', \'B\', \'C\', or \'D\'                ')
            print('                    Then press Enter.                    ')
            print('*********************************************************')
            time.sleep(0.5)
            if A == True:
                print('Option A: The belief that religion should not play a role in government, education, or other public parts of society.')
                print('*********************************************************')
                time.sleep(0.5)
            if B == True:
                print('Option B: The belief that religion should play a role in government, education, and other parts of society.')
                print('*********************************************************')
                time.sleep(0.5)
            if C == True:
                print('Option C: A movement to break away from the Catholic Church and create a new form of Catholicism.')
                print('*********************************************************')
                time.sleep(0.5)
            if D == True:
                print('Option D: A group of people who isolated themselves from the rest of society to study science.')
                print('*********************************************************')
                time.sleep(0.5)
            ans = input('')
            ans = ans.lower()
            rans = str('a')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why? Answer no for more information on this question. Answer no for more information on this question.')
                q1 = False
                print('Answer yes or no')
                why = input('')
                why = why.lower()
                if why == 'no':
                    print('Secularism is a belief that religion should be separate of goverment, and other public life.')
                    print('Secularism is the idea that religion is for private life.')
                    time.sleep(2)
                    q1 = False
                    break
                elif why == 'yes':
                    print('Next question')
                    time.sleep(0.5)
                    q1 = False
                    break
            elif ans == 'b':
                print('Answer B is incorrect, ' + name + '.')
                print('Secularism is just the opposite of this.')
                time.sleep(5)
                B = False
                continue
            elif ans == 'c':
                print('Answer C is incorrect, ' + name + '.')
                print('This is Protestantism, not Secularism.')
                C = False
                continue
            elif ans == 'd':
                print('Answer D is incorrect, ' + name + '.')
                print('This is Social Isolation, not Secularism.')
                D = False
                continue
            else:
                print('\'' + ans + '\' is not an option.')
                continue
        A = True
        B = True
        C = True
        D = True
        while q2 == True:
            print('*********************************************************')
            print('                      Question: 2                        ')
            print('*********************************************************')
            print(' Humanism is a system of values and beliefs that is based')
            print('   on the idea that people are basically good and that   ')
            print(' problems can be solved using reason instead of religion.')
            print('*********************************************************')
            time.sleep(2)
            print('                     Choose A or B                       ')
            print('*********************************************************')
            if A == True:
                print('Option A: True')
                print('*********************************************************')
            if B == True:
                print('Option B: False')
                print('*********************************************************')
            ans = input()
            ans = ans.lower()
            rans = str('a')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why? Answer no for more information on this question.')
                q1 = False
                print('Answer yes or no')
                why = input('')
                why = why.lower()
                if why == 'no':
                    print('Humanism was an appreciation of Humans and in the power of the human mind.')
                    time.sleep(5)
                    break
                if why == 'yes':
                    print('Next Question')
                    time.sleep(2)
                    break
            elif ans == 'b':
                print('Answer B is incorrect, ' + name + '.')
                print('Humanism was an appreciation of Humans and in the power of the human mind.')
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
            print('                      Question: 3                        ')
            print('*********************************************************')
            print('How are Secularism and Humanism reflected in the Gutenberg Bible?         ')
            print('*********************************************************')
            print('               Type \'A\', \'B\', \'C\', or \'D\'                ')
            print('*********************************************************')
            print('')
            print('')
            time.sleep(2)
            root = Tk()
            URL = "http://3.bp.blogspot.com/-Y-VdIkzl1V8/UAAyo1PsJFI/AAAAAAAABQo/HEcCJ2uFT_Q/s1600/gbible.gif"
            a = urllib.request.urlopen(URL)
            RI = a.read()
            a.close()
            b = base64.encodestring(RI)
            image = PhotoImage(data=b)
            label = Label(image=image)
            label.pack()
            root.mainloop()
            time.sleep(2)
            print('')
            print('')
            if A == True:
                print('Option A: The Gutenberg bible took power away from the Peasants by making the Church\'s power more widespread')
                print('than before. They had bibles everywhere now, and their religion was spreading.')
                print('*********************************************************')
                time.sleep(0.5)
            if B == True:
                print('Option B: Only humanism is reflected in the Gutenberg Bible')
                print('*********************************************************')
                time.sleep(0.5)
            if C == True:
                print('Option C: The Gutenberg Bible took away some of the Catholic Church\'s power')
                print('by taking away the power of the Priests to interpret the bible for the people.')
                print('*********************************************************')
                time.sleep(0.5)
            if D == True:
                print('Option D: They are not.')
                print('*********************************************************')
                time.sleep(0.5)
            ans = input('')
            ans = ans.lower()
            rans = str('c')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why? Answer no for more information on this question.')
                q1 = False
                print('Answer yes or no')
                why = input('')
                why = why.lower()
                if why == 'no':
                    print('The Gutenberg bible represents Humanism and Secularism because it helped disperse some of their power over the people, which was also one of the goals of Humanism and Secularism.')
                    time.sleep(0.5)
                    print('checkpoint')
                    break
                if why == 'yes':
                    print('Next Question')
                    time.sleep(2)
                    break
            elif ans == 'a':
                print('Answer A is incorrect, ' + name + '.')
                print('The Gutenberg bible represents Humanism and Secularism because it helped disperse some of their power over the people, which was also one of the goals of Humanism and Secularism.')
                A = False
                continue
            elif ans == 'b':
                print('Answer B is incorrect, ' + name + '.')
                print('The Gutenberg bible represents Humanism and Secularism because it helped disperse some of their power over the people, which was also one of the goals of Humanism and Secularism.')
                B = False
                continue
            elif ans == 'd':
                print('Answer D is incorrect, ' + name + '.')
                print('The Gutenberg bible represents Humanism and Secularism because it helped disperse some of their power over the people, which was also one of the goals of Humanism and Secularism.')
                D = False
                continue
            else:
                print('\'' + ans + '\' is not an option.')
                continue
        A = True
        B = True
        C = True
        D = True
        while q4 == True:
            print('*********************************************************')
            print('                      Question: 4                        ')
            print('*********************************************************')
            print(' Gutenberg was a German who invented the printing press. ')
            print('*********************************************************')
            print('                     Choose \'A\' or \'B\'                       ')
            print('*********************************************************')
            if A == True:
                print('Option A: True')
                print('*********************************************************')
            if B == True:
                print('Option B: False')
                print('*********************************************************')
            ans = input()
            ans = ans.lower()
            rans = str('a')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why? Answer no for more information on this question.')
                q1 = False
                print('Answer yes or no')
                why = input('')
                why = why.lower()
                if why == 'no':
                    print('Gutenberg invented the printing press in the year 1439, and was a German man.')
                    time.sleep(5)
                    break
                if why == 'yes':
                    print('Next Question')
                    time.sleep(2)
                    break
            elif ans == 'b':
                print('Answer B is incorrect, ' + name + '.')
                print('Gutenberg invented the printing press in the year 1439, and was a German man.')
                time.sleep(5)
                B = False
                continue
            else:
                print(ans + ' is not A or B')
                continue

        print('*********************************************************')
        print('                         Part: 2                         ')
        print('*********************************************************')
        print('                  Empires Outside Europe                 ')
        print('*********************************************************')
        print('                    Zheng He\'s FLeet                    ')
        print('*********************************************************')
        print('')
        print('')
        time.sleep(2)
        root = Tk()
        URL = "http://i.imgur.com/NzqDd25.gif"
        a = urllib.request.urlopen(URL)
        RI = a.read()
        a.close()
        b = base64.encodestring(RI)
        image = PhotoImage(data=b)
        label = Label(image=image)
        label.pack()
        root.mainloop()
        A = True
        B = True
        C = True
        D = True
        while q5 == True:
            time.sleep(2)
            print('')
            print('')
            print('*********************************************************')
            print('                      Question: 5                        ')
            print('*********************************************************')
            print('Zheng He commanded fleets of hundreds of treasure ships during the seven voyages and had a crew of 2,800 men.        ')
            print('*********************************************************')
            print('                     Choose A or B                       ')
            print('*********************************************************')
            if A == True:
                print('Option A: True')
                print('*********************************************************')
            if B == True:
                print('Option B: False')
                print('*********************************************************')
            ans = input()
            ans = ans.lower()
            rans = str('a')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why? Answer no for more information on this question.')
                q5 = False
                print('Answer yes or no')
                why = input('')
                why = why.lower()
            if why == 'no':
                print('The fleets actually had 28,000 men.')
                time.sleep(5)
                break
            if why == 'yes':
                print('Next Question')
                time.sleep(2)
                q5 = False
                continue
            elif ans == 'b':
                print('Answer B is incorrect, ' + name + '.')
                print('The fleets actually had 28,000 men.')
                B = False
                continue
        else:
            print(ans + ' is not A or B')
            continue
        A = True
        B = True
        C = True
        D = True
        while q6 == True:
            print('*********************************************************')
            print('                      Question: 6                        ')
            print('*********************************************************')
            print('Zheng He\'s boats were said to be up to 450 ft long and 180 ft wide.')
            print('*********************************************************')
            print('                     Choose A or B                       ')
            print('*********************************************************')
            time.sleep(2)
            root = Tk()
            URL = "http://i.imgur.com/NzqDd25.gif"
            a = urllib.request.urlopen(URL)
            RI = a.read()
            a.close()
            b = base64.encodestring(RI)
            image = PhotoImage(data=b)
            label = Label(image=image)
            label.pack()
            root.mainloop()
            time.sleep(2)
            print('*********************************************************')
            if A == True:
                print('Option A: True')
                print('*********************************************************')
            if B == True:
                print('Option B: False')
                print('*********************************************************')
            ans = input()
            ans = ans.lower()
            rans = str('a')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why? Answer no for more information on this question.')
                q5 = False
                print('Answer yes or no')
                why = input('')
                why = why.lower()
                if why == 'no':
                    print('The largest ships were gigantic \'Treasure Ships\' and made Columbus\' ship look tiny.')
                    time.sleep(5)
                    break
                if why == 'yes':
                    print('Next Question')
                    time.sleep(2)
                    q6 = False
                    continue
            elif ans == 'b':
                print('Answer B is incorrect, ' + name + '.')
                print('The largest ships were gigantic \'Treasure Ships\' and made Columbus\' ship look tiny.')
                B = False
                continue
            else:
                print(ans + ' is not an \'A\' or a \'B\'')
                continue
        A = True
        B = True
        C = True
        D = True
        while q7 == True:
            print('*********************************************************')
            print('                      Question: 7                        ')
            print('*********************************************************')
            print('Based on the creation of these fleets and gigantic ships we can tell...')
            print('*********************************************************')
            print('               Type \'A\', \'B\', \'C\', or \'D\'                ')
            print('*********************************************************')
            time.sleep(2)
            if A == True:
                print('Option A: China did a lot of trading during this time period, with a lot of cargo.')
                print('*********************************************************')
                time.sleep(0.5)
            if B == True:
                print('Option B: China had many desireable goods that were wanted by other countries.')
                print('*********************************************************')
                time.sleep(0.5)
            if C == True:
                print('Option C: The voyages were state funded.')
                print('*********************************************************')
                time.sleep(0.5)
            if D == True:
                print('Option D: All of the above')
                print('*********************************************************')
                time.sleep(0.5)
            ans = input('')
            ans = ans.lower()
            rans = str('d')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why? Answer no for more information on this question.')
                q1 = False
                print('Answer yes or no')
                why = input('')
                why = why.lower()
                if why == 'no':
                    print('Because China is not a free market, and the State controls most of the money, it had to be State funded. Nobody else could have afforded it.')
                    time.sleep(0.5)
                    print('checkpoint')
                    break
                if why == 'yes':
                    print('Next Question')
                    time.sleep(2)
                    break
            elif ans == 'a':
                print('Answer A is incorrect, ' + name + '.')
                print('Because China is not a free market, and the State controls most of the money, it had to be State funded. Nobody else could have afforded it.')
                A = False
                continue
            elif ans == 'b':
                print('Answer B is incorrect, ' + name + '.')
                print('CBecause China is not a free market, and the State controls most of the money, it had to be State funded. Nobody else could have afforded it.')
                B = False
                continue
            elif ans == 'c':
                print('Answer C is incorrect, ' + name + '.')
                print('Because China is not a free market, and the State controls most of the money, it had to be State funded. Nobody else could have afforded it.')
                C = False
                continue
            else:
                print('\'' + ans + '\' is not an option.')
                continue
        A = True
        B = True
        C = True
        D = True
        while q8 == True:
            print('*********************************************************')
            print('                         Part: 3                         ')
            print('*********************************************************')
            print('                     Age of Discovery                    ')
            print('*********************************************************')
            print('                   World Changing Foods                  ')
            print('*********************************************************')
            print('')
            print('')
            print('East Indie Spices')
            time.sleep(2)
            root = Tk()
            URL = "http://i.imgur.com/QM3RwyT.gif"
            a = urllib.request.urlopen(URL)
            RI = a.read()
            a.close()
            b = base64.encodestring(RI)
            image = PhotoImage(data=b)
            label = Label(image=image)
            label.pack()
            root.mainloop()
            print('')
            time.sleep(2)
            print('')
            print('')
            print('*********************************************************')
            print('                      Question: 8                        ')
            print('*********************************************************')
            print('Columbus found America because he was looking for ______')
            print('*********************************************************')
            print('               Type \'A\', \'B\', \'C\', or \'D\'                ')
            print('*********************************************************')
            time.sleep(2)
            if A == True:
                print('Option A: India')
                print('*********************************************************')
                time.sleep(0.5)
            if B == True:
                print('Option B: America')
                print('*********************************************************')
                time.sleep(0.5)
            if C == True:
                print('Option C: The East indies')
                print('*********************************************************')
                time.sleep(0.5)
            if D == True:
                print('Option D: The West indies')
                print('*********************************************************')
                time.sleep(0.5)
            ans = input('')
            ans = ans.lower()
            rans = str('c')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why? Answer no for more information on this question.')
                q1 = False
                print('Answer yes or no')
                why = input('')
                why = why.lower()
                if why == 'no':
                    print('East Indie Spices caused a major change in the course of history. When Columbus found america he was looking for a cheaper route to get them.')
                    time.sleep(0.5)
                    print('checkpoint')
                    break
                if why == 'yes':
                    print('Next Question')
                    time.sleep(2)
                    break
            elif ans == 'a':
                print('Answer A is incorrect, ' + name + '.')
                print('East Indie spices are the artifact, and caused some major changes in history, like Columbus discovering America')
                A = False
                continue
            elif ans == 'b':
                print('Answer B is incorrect, ' + name + '.')
                print('East Indie spices are the artifact, and caused some major changes in history, like Columbus discovering America')
                B = False
                continue
            elif ans == 'd':
                print('Answer D is incorrect, ' + name + '.')
                print('East Indie spices are the artifact, and caused some major changes in history, like Columbus discovering America')
                C = False
                continue
            else:
                print('\'' + ans + '\' is not an option.')
                continue
        A = True
        B = True
        C = True
        D = True
        while q9 == True:
            root = Tk()
            URL = "http://i.imgur.com/QM3RwyT.gif"
            a = urllib.request.urlopen(URL)
            RI = a.read()
            a.close()
            b = base64.encodestring(RI)
            image = PhotoImage(data=b)
            label = Label(image=image)
            label.pack()
            root.mainloop()
            print('*********************************************************')
            print('                      Question: 9                        ')
            print('*********************************************************')
            print('Which food caused major change in history?')
            print('*********************************************************')
            print('               Type \'A\', \'B\', \'C\', or \'D\'                ')
            print('*********************************************************')
            time.sleep(2)
            if A == True:
                print('Option A: Corn')
                print('*********************************************************')
                time.sleep(0.5)
            if B == True:
                print('Option B: Bread')
                print('*********************************************************')
                time.sleep(0.5)
            if C == True:
                print('Option C: Potatos')
                print('*********************************************************')
                time.sleep(0.5)
            if D == True:
                print('Option D: All of the above')
                print('*********************************************************')
                time.sleep(0.5)
            ans = input('')
            ans = ans.lower()
            rans = str('d')
            if ans == rans:
                print('Good Job, ' + name + '. You got it right. Do you understand why? Answer no for more information on this question.')
                q1 = False
                print('Answer yes or no')
                why = input('')
                why = why.lower()
                if why == 'no':
                    print('Potatoes made it possible for surplus in the amount of food in Europe, and fueld their wars')
                    time.sleep(0.5)
                    print('checkpoint')
                    break
                if why == 'yes':
                    print('Next Question')
                    time.sleep(2)
                    break
            elif ans == 'a':
                print('Answer A is incorrect, ' + name + '.')
                print('Potatoes made it possible for surplus in the amount of food in Europe, and fueld their wars')
                A = False
                continue
            elif ans == 'b':
                print('Answer B is incorrect, ' + name + '.')
                print('Potatoes made it possible for surplus in the amount of food in Europe, and fueld their wars')
                B = False
                continue
            elif ans == 'c':
                print('Answer C is incorrect, ' + name + '.')
                print('Potatoes made it possible for surplus in the amount of food in Europe, and fueld their wars')
                C = False
                continue
            else:
                print('\'' + ans + '\' is not an option.')
                continue
        time.sleep(2)
        print('You have reached the end of the quiz')
        print('Good Job!')



        break

    elif ans == 'no':
        print('What is your name actually?')
        name = input('')

        continue

    else:
        print('Please answer with yes or no. ' + ans + ' is not yes or no.')
        print('Please try again.')
        time.sleep(0.5)
        continue
