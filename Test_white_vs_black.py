# -*- coding: utf-8 -*-
"""
Created on Thu May 18 15:30:02 2023

@author: iaros
"""

from functions import*
import pickle
import os

WNowherToGo = [False, False, False]
ww = False

BNowherToGo = [False, False, False]
wb = False

turn = 0
rndm = 0
wws = 0
wbs = 0

biser = []
BisUsed = []
for _ in range(43):
    biser.append(10)
    BisUsed.append(False)
biserW = []
BisUsedW = []
for _ in range(32):
    biserW.append(10)
    BisUsedW.append(False)
board = [['b', 'b', 'b'], ['_', '_', '_'], ['w', 'w', 'w']]
print('Restore progress?')
print("Accept(1)/Decline(0) Warning! Previous progress won't be saved.")
progress = input()
while not progress in {'1', '0'}:
    print('Proper input needed')
    print('Restore progress?')
    print("Accept(1)/Decline(0)")
    progress = input()
if progress == '1':
    if os.path.exists(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'biser1_list.pb')):
        with open("biser1_list.pb",'rb') as file:
            biser = pickle.load(file)
    else:
        for k in range(43):
            biser[k] = 10
        with open("biser1_list.pb",'wb') as file:
            pickle.dump(biser, file)
    if os.path.exists(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'biserW1_list.pb')):
        with open("biserW1_list.pb",'rb') as file:
            biserW = pickle.load(file)
    else:
        for kl in range(32):
            biserW[kl] = 10
        with open("biserW1_list.pb",'wb') as file:
            pickle.dump(biserW, file)
else:
    for k in range(43):
        biser[k] = 10
    for kl in range(32):
        biserW[kl] = 10
    r = input('Wipe progress? 1/0 ')
    while not r in {'1', '0'}:
        print('Proper input needed')
        r = input('Wipe progress? 1\0 ')
    if r == '1':
        with open("biser1_list.pb",'wb') as file:
            pickle.dump(biser, file)
        with open("biserW1_list.pb",'wb') as file:
            pickle.dump(biserW, file)
for x in range(500):
    print(x)
    print()
    turn = 0
    rndm = 0
    board = [['b', 'b', 'b'], ['_', '_', '_'], ['w', 'w', 'w']]
    WNowherToGo = [False, False, False]
    ww = False

    BNowherToGo = [False, False, False]
    wb = False
    
    for y in range(43):
        BisUsed[y] = False
    for yu in range(32):
        BisUsedW[yu] = False
    while True: 
        
        turn += 1
        wb,board,BisUsedW = wt_turn(turn, board, biserW, BisUsedW)
        if ww == True:
            break
        stch = 0
        for i in range(3):
            for j in range(3):
                if board[i][j] == 'b':
                    stch += 1
                    if j == 1 and i < 2:
                        st = board[(i + 1)][(j - 1)] != 'w'
                    if i < 2:
                        st1 = board[(i + 1)][j] == '_'
                    if (j == 2 or j == 1) and i < 2:
                        st2 = board[(i + 1)][(j - 1)] == 'w'
                    if (j == 0 or j == 1) and i < 2:
                        st3 = board[(i + 1)][(j + 1)]
                    if j == 2 and i < 2:
                       st4 = board[(i + 1)][(j - 1)]
                if i < 2 and board[i][j] == 'b' and board[(i + 1)][j] != '_':
                    if j == 0  and i < 2 and board[(i + 1)][(j + 1)] != 'w':
                        BNowherToGo[0] = True
                    elif j == 2 and i < 2 and st4 != 'w':
                        BNowherToGo[2] = True
                    elif j == 1 and i < 2 and st3 != 'w' and st:
                        BNowherToGo[1] = True
                if board[i][j] == 'b':
                    if j == 0  and i < 2 and (st3 == 'w' or st1):
                        BNowherToGo[0] = False
                    elif j == 2 and i < 2 and (st4 == 'w' or st1):
                        BNowherToGo[2] = False
                    elif j == 1 and i < 2 and (st3 == 'w' or st2 or st1):
                        BNowherToGo[1] = False
        for g in range(3):
            etn = board[0][g] + board[1][g] + board[2][g]
            if not('b' in etn) and stch == 2:
                BNowherToGo[g] = True
            elif not('b' in etn) and stch == 1:
                BNowherToGo[g] = True
            elif not('b' in etn) and stch == 0:
                BNowherToGo[g] = True

        if 'w' in board[0] or all(BNowherToGo):
            ww = True
            print()
            break
        ww,board,BisUsed = bl_turn(turn, board, biser, BisUsed)
        if wb == True:
            break
        stch1 = 0
        for i1 in range(3):
            for j1 in range(3):
                if board[i1][j1] == 'w':
                    stch1 += 1
                    if j1 == 1 and i1 > 0:
                        st0 = board[(i1 - 1)][(j1 - 1)] != 'b'
                    if i1 > 0:
                        st11 = board[(i1 - 1)][j1] == '_'
                    if (j1 == 2 or j1 == 1) and i1 > 0:
                        st21 = board[(i1 - 1)][(j1 - 1)] == 'b'
                    if (j1 == 0 or j1 == 1) and i1 > 0:
                        st31 = board[(i1 - 1)][(j1 + 1)]
                    if j1 == 2 and i1 > 0:
                        st41 = board[(i1 - 1)][(j1 - 1)]
                if i1 > 0 and board[i1][j1] == 'w' and board[(i1 - 1)][j1] != '_':
                    if j1 == 0  and i1 > 0 and board[(i1 - 1)][(j1 + 1)] != 'b':
                        WNowherToGo[0] = True
                    elif j1 == 2 and i1 > 0 and st41 != 'b':
                        WNowherToGo[2] = True
                    elif j1 == 1 and i1 > 0 and st31 != 'b' and st0:
                        WNowherToGo[1] = True
                if board[i1][j1] == 'w':
                    if j1 == 0  and i1 > 0 and (st31 == 'b' or st11):
                        WNowherToGo[0] = False
                    elif j1 == 2 and i1 > 0 and (st41 == 'b' or st11):
                        WNowherToGo[2] = False
                    elif j1 == 1 and i1 > 0 and (st31 == 'b' or st21 or st11):
                        WNowherToGo[1] = False
        for g1 in range(3):
            etn1 = board[0][g1] + board[1][g1] + board[2][g1]
            if not('w' in etn1) and stch1 == 2:
                WNowherToGo[g1] = True
            elif not('w' in etn1) and stch1 == 1:
                WNowherToGo[g1] = True
            elif not('w' in etn1) and stch1 == 0:
                WNowherToGo[g1] = True
            
        if 'b' in board[2] or all(WNowherToGo):
            wb = True
            break
        
    if ww == True:
        wws += 1
        if progress == '1' or r == '1':
            for rturn in range(42, -1, -1):
                if BisUsed[rturn] == True:
                    biser[rturn] = biser[rturn] - 1
                    with open("biser1_list.pb",'wb') as file:
                        pickle.dump(biser, file)
                    break
        print('Whites Won')
        print(*biserW)
    else:
        wbs += 1
        if progress == '1' or r == '1':
            for rturnW in range(31, -1, -1):
                if BisUsedW[rturnW] == True:
                    biserW[rturnW] = biserW[rturnW] - 1
                    with open("biserW1_list.pb",'wb') as file:
                        pickle.dump(biserW, file)
                    break
        print('Blacks Won')
        print(*biser)
print('White')
print()
print(*biserW)
print()
print(wws)
print()
print('Black')
print()
print(*biser)
print()
print(wbs)
