# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:09:07 2023

@author: iaros
"""
from functions import*
import pickle

wt = ''
WNowherToGo = [False, False, False]
ww = False

BNowherToGo = [False, False, False]
wb = False

turn = 0
rndm = 0

biser = []
BisUsed = []
for _ in range(43):
    biser.append(10)
    BisUsed.append(False)

board = [['b', 'b', 'b'], ['_', '_', '_'], ['w', 'w', 'w']]
print('Restore progress?')
print("Accept(1)/Decline(0) Warning! Progress won't be saved.")
progress = input()
while not progress in {'1', '0'}:
    print('Proper input needed')
    print('Restore progress?')
    print("Accept(1)/Decline(0) Warning! Previous progress won't be saved.")
    progress = input()
if progress == '1':
    with open("biser1_list.pb",'rb') as file:
        biser = pickle.load(file)
else:
    for k in range(43):
        biser[k] = 10
    r = input('Wipe progress? 1/0 ')
    while not r in {'1', '0'}:
        print('Proper input needed')
        r = input('Wipe progress? 1/0 ')
    if r == '1':
        with open("biser1_list.pb",'wb') as file:
            pickle.dump(biser, file)
while True: 
    turn += 1
    print('White turn')
    print()
    for line in board: print(*line)
    wt = input('y:x.y:x ')
    print()
    
    while not is_valid(wt):
        for line in board: print(*line)
        print()
        print('proper coordinats needed')
        wt = input('y:x.y:x ')
        print()
        
    while not valid_turn(board, wt):
        for line in board: print(*line)
        print()
        print('proper coordinats needed')
        wt = input('y:x.y:x ')
        print()
        
        while not is_valid(wt):
            for line in board: print(*line)
            print()
            print('proper coordinats needed')
            wt = input('y:x.y:x ')
            print()
    
    y0,x0,y1,x1=[int(c) -1  for c in wt[::2] ]
    board[y0][x0] = '_'
    board[y1][x1] = 'w'
    
    for line in board: print(*line)
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
    if ww == True:
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
        break
if ww == True:
    if progress == '1' or r == '1':
        for rturn in range(42, -1, -1):
            if BisUsed[rturn] == True:
                biser[rturn] = biser[rturn] - 1
                with open("biser1_list.pb",'wb') as file:
                    pickle.dump(biser, file)
                break
    print('You Won')
    print(*biser)
else:
    print('Game Over')
