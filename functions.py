# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:30:58 2023

@author: iaros
"""

from random import randint
#%%
def is_valid (wt):
    
    if len(wt) < 7:
        wt = '_______'
    valid = wt[1::2] == ':.:'
    all([c in '123' for c in wt[::2]])
    
    return all([c in '123' for c in wt[::2]]) and valid
#%%
def valid_turn(board, wt):
    y0,x0,y1,x1=[int(c) -1  for c in wt[::2]]
    flagobshw1 = board[y0][x0] == 'w'
    flagobshw2 = board[y1][x1] != 'w'
    flagobshw3 = y0 == y1 + 1 and flagobshw2

    flagforward1 = board[y1][x1] != 'b'
    flagforward = x0 == x1 and flagforward1

    flageats = x0 == x1 + 1 or x0 == x1 - 1
    alwflag = flagobshw1 and flagobshw3
    
    return alwflag and (flagforward or not(flagforward1) and flageats)

#%%
def bl_turn(turn, board, biser, BisUsed):
    rndm = 0
    ww = False
    print()
    print('Black turn')
    print()
    if turn == 1:
        if board[1][0] == 'w' or board[1][2] == 'w':
            if not biser[0] + biser[1] + biser[2] - 1 <= 0:
                rndm = randint(0, biser[0] + biser[1] + biser[2] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[1][0] == 'w':
                if rndm < biser[0]:
                    board[1][0] = 'b'
                    board[0][1] = '_'
                    BisUsed[0] = True
                elif rndm >= biser[0] and rndm < biser[0] + biser[1]:
                    board[1][1] = 'b'
                    board[0][1] = '_'
                    BisUsed[1] = True
                elif rndm >= biser[0] + biser[1] and rndm < biser[0] + biser[1] + biser[2]:
                    board[1][2] = 'b'
                    board[0][2] = '_'
                    BisUsed[2] = True
            else:
                if rndm < biser[0]:
                    board[1][2] = 'b'
                    board[0][1] = '_'
                    BisUsed[0] = True
                elif rndm >= biser[0] and rndm < biser[0] + biser[1]:
                    board[1][1] = 'b'
                    board[0][1] = '_'
                    BisUsed[1] = True
                elif rndm >= biser[0] + biser[1] and rndm < biser[0] + biser[1] + biser[2]:
                    board[1][0] = 'b'
                    board[0][0] = '_'
                    BisUsed[2] = True
        else:
            if not biser[3] + biser[4] - 1 <= 0:
                rndm = randint(0, biser[3] + biser[4] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if rndm < biser[3]:
                board[1][0] = 'b'
                board[0][0] = '_'
                BisUsed[3] = True
            elif rndm >= biser[3] and rndm < biser[3] + biser[4]:
                board[1][1] = 'b'
                board[0][0] = '_'
                BisUsed[4] = True
    elif turn == 2:
        if board == [['b', '_', 'b'], ['b', 'w', '_'], ['_', '_', 'w']] or board == [['b', '_', 'b'], ['_', 'w', 'b'], ['w', '_', '_']]:
            if not biser[5] + biser[6] + biser[7] + biser[8] - 1 <= 0:
                rndm = randint(0, biser[5] + biser[6] + biser[7] + biser[8] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if  board[2][2] == 'w':
                if rndm < biser[5]:
                    board[2][0] = 'b'
                    board[1][0] = '_'
                    BisUsed[5] = True
                elif rndm >= biser[5] and rndm < biser[5] + biser[6]:
                    board[1][1] = 'b'
                    board[0][0] = '_'
                    BisUsed[6] = True
                elif rndm >= biser[5] + biser[6] and rndm < biser[5] + biser[6] + biser[7]:
                    board[1][1] = 'b'
                    board[0][2] = '_'
                    BisUsed[7] = True
                elif rndm >= biser[5] + biser[6] + biser[7] and rndm < biser[5] + biser[6] + biser[7] + biser[8]:
                    board[1][2] = 'b'
                    board[0][2] = '_'
                    BisUsed[8] = True
            else:
                if rndm < biser[5]:
                    board[2][2] = 'b'
                    board[1][2] = '_'
                    BisUsed[5] = True
                elif rndm >= biser[5] and rndm < biser[5] + biser[6]:
                    board[1][1] = 'b'
                    board[0][2] = '_'
                    BisUsed[6] = True
                elif rndm >= biser[5] + biser[6] and rndm < biser[5] + biser[6] + biser[7]:
                    board[1][1] = 'b'
                    board[0][0] = '_'
                    BisUsed[7] = True
                elif rndm >= biser[5] + biser[6] + biser[7] and rndm < biser[5] + biser[6] + biser[7] + biser[8]:
                    board[1][0] = 'b'
                    board[0][0] = '_'
                    BisUsed[8] = True
        if board == [['_', 'b', 'b'], ['w', 'b', '_'], ['_', '_', 'w']] or board == [['b', 'b', '_'], ['_', 'b', 'w'], ['w', '_', '_']]:
            if not biser[9] + biser[10] + biser[11] + biser[12] - 1 <= 0:
                rndm = randint(0, biser[9] + biser[10] + biser[11] + biser[12] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if  board[2][2] == 'w':
                if rndm < biser[9]:
                    board[1][0] = 'b'
                    board[0][1] = '_'
                    BisUsed[9] = True
                elif rndm >= biser[9] and rndm < biser[9] + biser[10]:
                    board[2][1] = 'b'
                    board[1][1] = '_'
                    BisUsed[10] = True
                elif rndm >= biser[9] + biser[10] and rndm < biser[9] + biser[10] + biser[11]:
                    board[1][2] = 'b'
                    board[0][2] = '_'
                    BisUsed[11] = True
                elif rndm >= biser[9] + biser[10] + biser[11] and rndm < biser[9] + biser[10] + biser[11] + biser[12]:
                    board[2][2] = 'b'
                    board[1][1] = '_'
                    BisUsed[12] = True
            else:
                if rndm < biser[9]:
                    board[1][2] = 'b'
                    board[0][1] = '_'
                    BisUsed[9] = True
                elif rndm >= biser[9] and rndm < biser[9] + biser[10]:
                    board[2][1] = 'b'
                    board[1][1] = '_'
                    BisUsed[10] = True
                elif rndm >= biser[9] + biser[10] and rndm < biser[9] + biser[10] + biser[11]:
                    board[1][0] = 'b'
                    board[0][0] = '_'
                    BisUsed[11] = True
                elif rndm >= biser[9] + biser[10] + biser[11] and rndm < biser[9] + biser[10] + biser[11] + biser[12]:
                    board[2][0] = 'b'
                    board[1][1] = '_'
                    BisUsed[12] = True
        if board == [['b', '_', 'b'], ['w', 'w', '_'], ['_', 'w', '_']] or board == [['b', '_', 'b'], ['_', 'w', 'w'], ['_', 'w', '_']]:
            if not biser[13] + biser[14] + biser[15] - 1 <= 0:
                rndm = randint(0, biser[13] + biser[14] + biser[15] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[1][0] == 'w':
                if rndm < biser[13]:
                    board[1][1] = 'b'
                    board[0][0] = '_'
                    BisUsed[13] = True
                elif rndm >= biser[13] and rndm < biser[13] + biser[14]:
                    board[1][1] = 'b'
                    board[0][2] = '_'
                    BisUsed[14] = True
                elif rndm >= biser[13] + biser[14] and rndm < biser[13] + biser[14] + biser[15]:
                    board[1][2] = 'b'
                    board[0][2] = '_'
                    BisUsed[15] = True
            else:
                if rndm < biser[13]:
                    board[1][1] = 'b'
                    board[0][2] = '_'
                    BisUsed[13] = True
                elif rndm >= biser[13] and rndm < biser[13] + biser[14]:
                    board[1][1] = 'b'
                    board[0][0] = '_'
                    BisUsed[14] = True
                elif rndm >= biser[13] + biser[14] and rndm < biser[13] + biser[14] + biser[15]:
                    board[1][0] = 'b'
                    board[0][0] = '_'
                    BisUsed[15] = True
        if board == [['b', 'b', '_'], ['w', '_', 'w'], ['_', '_', 'w']] or board == [['_', 'b', 'b'], ['w', '_', 'w'], ['w', '_', '_']]:
            if not biser[16] + biser[17] + biser[18] - 1 <= 0:
                rndm = randint(0, biser[16] + biser[17] + biser[18] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[2][1] == 'w':
                if rndm < biser[16]:
                    board[1][0] = 'b'
                    board[0][1] = '_'
                    BisUsed[16] = True
                elif rndm >= biser[16] and rndm < biser[16] + biser[17]:
                    board[1][1] = 'b'
                    board[0][1] = '_'
                    BisUsed[17] = True
                elif rndm >= biser[16] + biser[17] and rndm < biser[16] + biser[17] + biser[18]:
                    board[1][2] = 'b'
                    board[0][1] = '_'
                    BisUsed[18] = True
            else:
                if rndm < biser[16]:
                    board[1][2] = 'b'
                    board[0][1] = '_'
                    BisUsed[16] = True
                elif rndm >= biser[16] and rndm < biser[16] + biser[17]:
                    board[1][1] = 'b'
                    board[0][1] = '_'
                    BisUsed[17] = True
                elif rndm >= biser[16] + biser[17] and rndm < biser[16] + biser[17] + biser[18]:
                    board[1][0] = 'b'
                    board[0][1] = '_'
                    BisUsed[18] = True
        if board == [['_', 'b', 'b'], ['_', 'b', 'w'], ['w', '_', '_']] or board == [['b', 'b', '_'], ['w', 'b', '_'], ['_', '_', 'w']]:
            if not biser[19] + biser[20] + biser[21] - 1 <= 0:
                rndm = randint(0, biser[19] + biser[20] + biser[21] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[2][0] == 'w':
                if rndm < biser[19]:
                    board[2][0] = 'b'
                    board[1][1] = '_'
                    BisUsed[19] = True
                elif rndm >= biser[19] and rndm < biser[19] + biser[20]:
                    board[2][1] = 'b'
                    board[1][1] = '_'
                    BisUsed[20] = True
                elif rndm >= biser[19] + biser[20] and rndm < biser[19] + biser[20] + biser[21]:
                    board[1][2] = 'b'
                    board[0][1] = '_'
                    BisUsed[21] = True
            else:
                if rndm < biser[19]:
                    board[2][2] = 'b'
                    board[1][1] = '_'
                    BisUsed[19] = True
                elif rndm >= biser[19] and rndm < biser[19] + biser[20]:
                    board[2][1] = 'b'
                    board[1][1] = '_'
                    BisUsed[20] = True
                elif rndm >= biser[19] + biser[20] and rndm < biser[19] + biser[20] + biser[21]:
                    board[1][0] = 'b'
                    board[0][1] = '_'
                    BisUsed[21] = True
        if board == [['_', 'b', 'b'], ['b', 'w', 'w'], ['w', '_', '_']] or board == [['b', 'b', '_'], ['w', 'w', 'b'], ['_', '_', 'w']]:
            if not biser[22] + biser[23] - 1 <= 0:
                rndm = randint(0, biser[22] + biser[23] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[2][0] == 'w':
                if rndm < biser[22]:
                    board[1][2] = 'b'
                    board[0][1] = '_'
                    BisUsed[22] = True
                elif rndm >= biser[22] and rndm < biser[22] + biser[23]:
                    board[1][1] = 'b'
                    board[0][2] = '_'
                    BisUsed[23] = True
            else:
                if rndm < biser[22]:
                    board[1][0] = 'b'
                    board[0][1] = '_'
                    BisUsed[22] = True
                elif rndm >= biser[22] and rndm < biser[22] + biser[23]:
                    board[1][1] = 'b'
                    board[0][0] = '_'
                    BisUsed[23] = True
        if board == [['b', '_', 'b'], ['b', '_', 'w'], ['_', 'w', '_']] or board == [['b', '_', 'b'], ['w', '_', 'b'], ['_', 'w', '_']]:
            if not biser[24] + biser[25] - 1 <= 0:
                rndm = randint(0, biser[24] + biser[25] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[1][2] == 'w':
                if rndm < biser[24]:
                    board[2][0] = 'b'
                    board[1][0] = '_'
                    BisUsed[24] = True
                elif rndm >= biser[24] and rndm < biser[24] + biser[25]:
                    board[2][1] = 'b'
                    board[1][0] = '_'
                    BisUsed[25] = True
            else:
                if rndm < biser[24]:
                    board[2][2] = 'b'
                    board[1][2] = '_'
                    BisUsed[24] = True
                elif rndm >= biser[24] and rndm < biser[24] + biser[25]:
                    board[2][1] = 'b'
                    board[1][2] = '_'
                    BisUsed[25] = True
        if board == [['_', 'b', 'b'], ['_', 'w', '_'], ['_', '_', 'w']] or board == [['b', 'b', '_'], ['_', 'w', '_'], ['w', '_', '_']]:
            if not biser[26] + biser[27] - 1 <= 0:
                rndm = randint(0, biser[26] + biser[27] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[2][2] == 'w':
                if rndm < biser[26]:
                    board[1][1] = 'b'
                    board[0][2] = '_'
                    BisUsed[26] = True
                elif rndm >= biser[26] and rndm < biser[26] + biser[27]:
                    board[1][2] = 'b'
                    board[0][2] = '_'
                    BisUsed[27] = True
            else:
                if rndm < biser[26]:
                    board[1][1] = 'b'
                    board[0][0] = '_'
                    BisUsed[26] = True
                elif rndm >= biser[26] and rndm < biser[26] + biser[27]:
                    board[1][0] = 'b'
                    board[0][0] = '_'
                    BisUsed[27] = True
        if board == [['_', 'b', 'b'], ['_', 'w', '_'], ['w', '_', '_']] or board == [['b', 'b', '_'], ['_', 'w', '_'], ['_', '_', 'w']]:
            if not biser[28] + biser[29] - 1 <= 0:
                rndm = randint(0, biser[28] + biser[29] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[2][0] == 'w':
                if rndm < biser[28]:
                    board[1][1] = 'b'
                    board[0][2] = '_'
                    BisUsed[28] = True
                elif rndm >= biser[28] and rndm < biser[28] + biser[29]:
                    board[1][2] = 'b'
                    board[0][2] = '_'
                    BisUsed[29] = True
            else:
                if rndm < biser[28]:
                    board[1][1] = 'b'
                    board[0][0] = '_'
                    BisUsed[28] = True
                elif rndm >= biser[28] and rndm < biser[28] + biser[29]:
                    board[1][0] = 'b'
                    board[0][0] = '_'
                    BisUsed[29] = True
        if board == [['b', '_', 'b'], ['w', '_', '_'], ['_', '_', 'w']] or board == [['b', '_', 'b'], ['_', '_', 'w'], ['w', '_', '_']]:
            if board[2][2] == 'w':
                board[1][2] = 'b'
                board[0][2] = '_'
            else:
                board[1][0] = 'b'
                board[0][0] = '_'
    else:
        if board == [['_', '_', 'b'], ['b', 'b', 'w'], ['_', '_', '_']] or board == [['b', '_', '_'], ['w', 'b', 'b'], ['_', '_', '_']]:
            if not biser[30] + biser[31] - 1 <= 0:
                rndm = randint(0, biser[30] + biser[31] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[1][2] == 'w':
                if rndm < biser[30]:
                    board[2][0] = 'b'
                    board[1][0] = '_'
                    BisUsed[30] = True
                elif rndm >= biser[30] and rndm < biser[30] + biser[31]:
                    board[2][1] = 'b'
                    board[1][1] = '_'
                    BisUsed[31] = True
            else:
                if rndm < biser[30]:
                    board[2][2] = 'b'
                    board[1][2] = '_'
                    BisUsed[30] = True
                elif rndm >= biser[30] and rndm < biser[30] + biser[31]:
                    board[2][1] = 'b'
                    board[1][1] = '_'
                    BisUsed[31] = True
        if board == [['b', '_', '_'], ['w', 'w', 'w'], ['_', '_', '_']] or board == [['_', '_', 'b'], ['w', 'w', 'w'], ['_', '_', '_']]:
            print('AI surrenders')
            ww = True
            print()
        if board == [['_', 'b', '_'], ['b', 'w', 'w'], ['_', '_', '_']] or board == [['_', 'b', '_'], ['w', 'w', 'b'], ['_', '_', '_']]:
            if not biser[32] + biser[33] - 1 <= 0:
                rndm = randint(0, biser[32] + biser[33] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[1][2] == 'w':
                if rndm < biser[32]:
                    board[2][0] = 'b'
                    board[1][0] = '_'
                    BisUsed[32] = True
                elif rndm >= biser[32] and rndm < biser[32] + biser[33]:
                    board[1][2] = 'b'
                    board[0][1] = '_'
                    BisUsed[33] = True
            else:
                if rndm < biser[32]:
                    board[2][2] = 'b'
                    board[1][2] = '_'
                    BisUsed[32] = True
                elif rndm >= biser[32] and rndm < biser[32] + biser[33]:
                    board[1][0] = 'b'
                    board[0][1] = '_'
                    BisUsed[33] = True
        if board == [['b', '_', '_'], ['b', 'b', 'w'], ['_', '_', '_']] or board == [['_', '_', 'b'], ['w', 'b', 'b'], ['_', '_', '_']]:
            if not biser[34] + biser[35] - 1 <= 0:
                rndm = randint(0, biser[34] + biser[35] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[1][2] == 'w':
                if rndm < biser[34]:
                    board[2][0] = 'b'
                    board[1][0] = '_'
                    BisUsed[34] = True
                elif rndm >= biser[34] and rndm < biser[34] + biser[35]:
                    board[2][1] = 'b'
                    board[1][1] = '_'
                    BisUsed[35] = True
            else:
                if rndm < biser[34]:
                    board[2][2] = 'b'
                    board[1][2] = '_'
                    BisUsed[34] = True
                elif rndm >= biser[34] and rndm < biser[34] + biser[35]:
                    board[2][1] = 'b'
                    board[1][1] = '_'
                    BisUsed[35] = True
        if board == [['_', '_', 'b'], ['b', 'w', '_'], ['_', '_', '_']] or board == [['b', '_', '_'], ['_', 'w', 'b'], ['_', '_', '_']]:
            if not biser[36] + biser[37] + biser[38] - 1 <= 0:
                rndm = randint(0, biser[36] + biser[37] + biser[38] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[0][2] == 'b':
                if rndm < biser[36]:
                    board[2][0] = 'b'
                    board[1][0] = '_'
                    BisUsed[36] = True
                elif rndm >= biser[36] and rndm < biser[36] + biser[37]:
                    board[1][1] = 'b'
                    board[0][2] = '_'
                    BisUsed[37] = True
                elif rndm >= biser[36] + biser[37] and rndm < biser[36] + biser[37] + biser[38]:
                    board[1][2] = 'b'
                    board[0][2] = '_'
                    BisUsed[38] = True
            else:
                if rndm < biser[36]:
                    board[2][2] = 'b'
                    board[1][2] = '_'
                    BisUsed[36] = True
                elif rndm >= biser[36] and rndm < biser[36] + biser[37]:
                    board[1][1] = 'b'
                    board[0][0] = '_'
                    BisUsed[37] = True
                elif rndm >= biser[36] + biser[37] and rndm < biser[36] + biser[37] + biser[38]:
                    board[1][0] = 'b'
                    board[0][0] = '_'
                    BisUsed[38] = True
        if board == [['_', 'b', '_'], ['w', 'b', '_'], ['_', '_', '_']] or board == [['_', 'b', '_'], ['_', 'b', 'w'], ['_', '_', '_']]:
            if not biser[39] + biser[40] - 1 <= 0:
                rndm = randint(0, biser[39] + biser[40] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[1][0] == 'w':
                if rndm < biser[39]:
                    board[1][0] = 'b'
                    board[0][1] = '_'
                    BisUsed[39] = True
                elif rndm >= biser[39] and rndm < biser[39] + biser[40]:
                    board[2][1] = 'b'
                    board[1][1] = '_'
                    BisUsed[40] = True
            else:
                if rndm < biser[39]:
                    board[1][2] = 'b'
                    board[0][1] = '_'
                    BisUsed[39] = True
                elif rndm >= biser[39] and rndm < biser[39] + biser[40]:
                    board[2][1] = 'b'
                    board[1][1] = '_'
                    BisUsed[40] = True
        if board == [['b', '_', '_'], ['b', 'w', '_'], ['_', '_', '_']] or board == [['_', '_', 'b'], ['_', 'w', 'b'], ['_', '_', '_']]:
            if not biser[41] + biser[42] - 1 <= 0:
                rndm = randint(0, biser[41] + biser[42] - 1)
            else:
                print('AI surrenders')
                ww = True
                print()
            if board[1][0] == 'b':
                if rndm < biser[41]:
                    board[1][1] = 'b'
                    board[0][0] = '_'
                    BisUsed[41] = True
                elif rndm >= biser[41] and rndm < biser[41] + biser[42]:
                    board[2][0] = 'b'
                    board[1][0] = '_'
                    BisUsed[42] = True
            else:
                if rndm < biser[41]:
                    board[1][1] = 'b'
                    board[0][2] = '_'
                    BisUsed[41] = True
                elif rndm >= biser[41] and rndm < biser[41] + biser[42]:
                    board[2][2] = 'b'
                    board[1][2] = '_'
                    BisUsed[42] = True
    for line in board: print(*line)
    print()
    return ww, board, BisUsed
#%%
def wt_turn(turn, board, biserW, BisUsedW):
    rndm = 0
    wb = False
    print()
    print('White turn')
    print()
    if turn == 1:
        if not biserW[0] + biserW[1] - 1 <= 0:
                rndm = randint(0, biserW[1] + biserW[0] - 1)
        else:
            print('AI surrenders')
            wb = True
            print()
        if rndm < biserW[0]:
            board[1][1] = 'w'
            board[2][1] = '_'
            BisUsedW[0] = True
        elif rndm >= biserW[0] and rndm < biserW[0] + biserW[1]:
            if randint(0, 1) == 0:
                board[1][0] = 'w'
                board[2][0] = '_'
            else:
                board[1][2] = 'w'
                board[2][2] = '_'
            BisUsedW[1] = True
    elif turn == 2:
        if board == [['b', '_', 'b'], ['b', '_', '_'], ['_', 'w', 'w']] or board == [['b', '_', 'b'], ['_', '_', 'b'], ['w', 'w', '_']]:
            if not biserW[2] + biserW[3] + biserW[4] - 1 <= 0:
                rndm = randint(0, biserW[2] + biserW[3] + biserW[4] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[2][2] == 'w':
                if rndm < biserW[2]:
                    board[1][0] = 'w'
                    board[2][1] = '_'
                    BisUsedW[2] = True
                elif rndm >= biserW[2] and rndm < biserW[2] + biserW[3]:
                    board[1][1] = 'w'
                    board[2][1] = '_'
                    BisUsedW[3] = True
                elif rndm >= biserW[2] + biserW[3] and rndm < biserW[2] + biserW[3] + biserW[4]:
                    board[1][2] = 'w'
                    board[2][2] = '_'
                    BisUsedW[4] = True
            else:
                if rndm < biserW[2]:
                    board[1][2] = 'w'
                    board[2][1] = '_'
                    BisUsedW[2] = True
                elif rndm >= biserW[2] and rndm < biserW[2] + biserW[3]:
                    board[1][1] = 'w'
                    board[2][1] = '_'
                    BisUsedW[3] = True
                elif rndm >= biserW[2] + biserW[3] and rndm < biserW[2] + biserW[3] + biserW[4]:
                    board[1][0] = 'w'
                    board[2][0] = '_'
                    BisUsedW[4] = True
        if board == [['b', '_', 'b'], ['w', 'b', '_'], ['_', 'w', 'w']] or board == [['b', '_', 'b'], ['_', 'b', 'w'], ['w', 'w', '_']]:
            if not biserW[5] + biserW[6] - 1 <= 0:
                rndm = randint(0, biserW[5] + biserW[6] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[2][2] == 'w':
                if rndm < biserW[5]:
                    board[1][1] = 'w'
                    board[2][2] = '_'
                    BisUsedW[5] = True
                elif rndm >= biserW[5] and rndm < biserW[5] + biserW[6]:
                    board[1][2] = 'w'
                    board[2][2] = '_'
                    BisUsedW[6] = True
            else:
                if rndm < biserW[5]:
                    board[1][1] = 'w'
                    board[2][0] = '_'
                    BisUsedW[5] = True
                elif rndm >= biserW[5] and rndm < biserW[5] + biserW[6]:
                    board[1][0] = 'w'
                    board[2][0] = '_'
                    BisUsedW[6] = True
        if board == [['b', 'b', '_'], ['w', '_', 'b'], ['_', 'w', 'w']] or board == [['_', 'b', 'b'], ['b', '_', 'w'], ['w', 'w', '_']]:
            if not biserW[7] + biserW[8] + biserW[9] - 1 <= 0:
                rndm = randint(0, biserW[7] + biserW[8] + biserW[9] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[2][2] == 'w':
                if rndm < biserW[7]:
                    board[0][1] = 'w'
                    board[1][0] = '_'
                    BisUsedW[7] = True
                elif rndm >= biserW[7] and rndm < biserW[7] + biserW[8]:
                    board[1][1] = 'w'
                    board[2][1] = '_'
                    BisUsedW[8] = True
                elif rndm >= biserW[7] + biserW[8] and rndm < biserW[7] + biserW[8] + biserW[9]:
                    board[1][2] = 'w'
                    board[2][1] = '_'
                    BisUsedW[9] = True
            else:
                if rndm < biserW[7]:
                    board[0][1] = 'w'
                    board[1][2] = '_'
                    BisUsedW[7] = True
                elif rndm >= biserW[7] and rndm < biserW[7] + biserW[8]:
                    board[1][1] = 'w'
                    board[2][1] = '_'
                    BisUsedW[8] = True
                elif rndm >= biserW[7] + biserW[8] and rndm < biserW[7] + biserW[8] + biserW[9]:
                    board[1][0] = 'w'
                    board[2][1] = '_'
                    BisUsedW[9] = True
        if board == [['_', 'b', 'b'], ['b', 'w', '_'], ['w', '_', 'w']] or board == [['b', 'b', '_'], ['_', 'w', 'b'], ['w', '_', 'w']]:
            if not biserW[10] + biserW[11] - 1 <= 0:
                rndm = randint(0, biserW[10] + biserW[11] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[1][0] == 'b':
                if rndm < biserW[10]:
                    board[0][2] = 'w'
                    board[1][1] = '_'
                    BisUsedW[10] = True
                elif rndm >= biserW[10] and rndm < biserW[10] + biserW[11]:
                    board[1][2] = 'w'
                    board[2][2] = '_'
                    BisUsedW[11] = True
            else:
                if rndm < biserW[10]:
                    board[0][0] = 'w'
                    board[1][1] = '_'
                    BisUsedW[10] = True
                elif rndm >= biserW[10] and rndm < biserW[10] + biserW[11]:
                    board[1][0] = 'w'
                    board[2][0] = '_'
                    BisUsedW[11] = True
        if board == [['_', 'b', 'b'], ['_', 'b', '_'], ['w', '_', 'w']] or board == [['b', 'b', '_'], ['_', 'b', '_'], ['w', '_', 'w']]:
            if not biserW[12] + biserW[13] + biserW[14] + biserW[15] - 1 <= 0:
                rndm = randint(0, biserW[12] + biserW[13] + biserW[14] + biserW[15] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[0][2] == 'b':
                if rndm < biserW[12]:
                    board[1][0] = 'w'
                    board[2][0] = '_'
                    BisUsedW[12] = True
                elif rndm >= biserW[12] and rndm < biserW[12] + biserW[13]:
                    board[1][1] = 'w'
                    board[2][0] = '_'
                    BisUsedW[13] = True
                elif rndm >= biserW[12] + biserW[13] and rndm < biserW[12] + biserW[13] + biserW[14]:
                    board[1][1] = 'w'
                    board[2][2] = '_'
                    BisUsedW[14] = True
                elif rndm >= biserW[12] + biserW[13] + biserW[14] and rndm < biserW[12] + biserW[13] + biserW[14] + biserW[15]:
                    board[1][2] = 'w'
                    board[2][2] = '_'
                    BisUsedW[15] = True
            else:
                if rndm < biserW[12]:
                    board[1][2] = 'w'
                    board[2][2] = '_'
                    BisUsedW[12] = True
                elif rndm >= biserW[12] and rndm < biserW[12] + biserW[13]:
                    board[1][1] = 'w'
                    board[2][2] = '_'
                    BisUsedW[13] = True
                elif rndm >= biserW[12] + biserW[13] and rndm < biserW[12] + biserW[13] + biserW[14]:
                    board[1][1] = 'w'
                    board[2][0] = '_'
                    BisUsedW[14] = True
                elif rndm >= biserW[12] + biserW[13] + biserW[14] and rndm < biserW[12] + biserW[13] + biserW[14] + biserW[15]:
                    board[1][0] = 'w'
                    board[2][0] = '_'
                    BisUsedW[15] = True
    elif turn == 3:
        if board == [['_', '_', 'b'], ['b', 'b', '_'], ['_', '_', 'w']] or board == [['b', '_', '_'], ['_', 'b', 'b'], ['w', '_', '_']]:
            if not biserW[16] + biserW[17] - 1 <= 0:
                rndm = randint(0, biserW[16] + biserW[17] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[2][2] == 'w':
                if rndm < biserW[16]:
                    board[1][1] = 'w'
                    board[2][2] = '_'
                    BisUsedW[16] = True
                elif rndm >= biserW[16] and rndm < biserW[16] + biserW[17]:
                    board[1][2] = 'w'
                    board[2][2] = '_'
                    BisUsedW[17] = True
            else:
                if rndm < biserW[16]:
                    board[1][1] = 'w'
                    board[2][0] = '_'
                    BisUsedW[16] = True
                elif rndm >= biserW[16] and rndm < biserW[16] + biserW[17]:
                    board[1][0] = 'w'
                    board[2][0] = '_'
                    BisUsedW[17] = True
        if board == [['b', '_', '_'], ['b', 'b', '_'], ['_', '_', 'w']] or board == [['_', '_', 'b'], ['_', 'b', 'b'], ['w', '_', '_']]:
            if not biserW[18] + biserW[19] - 1 <= 0:
                rndm = randint(0, biserW[18] + biserW[19] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[2][2] == 'w':
                if rndm < biserW[18]:
                    board[1][1] = 'w'
                    board[2][2] = '_'
                    BisUsedW[18] = True
                elif rndm >= biserW[18] and rndm < biserW[18] + biserW[19]:
                    board[1][2] = 'w'
                    board[2][2] = '_'
                    BisUsedW[19] = True
            else:
                if rndm < biserW[18]:
                    board[1][1] = 'w'
                    board[2][0] = '_'
                    BisUsedW[18] = True
                elif rndm >= biserW[18] and rndm < biserW[18] + biserW[19]:
                    board[1][0] = 'w'
                    board[2][0] = '_'
                    BisUsedW[19] = True
        if board == [['b', '_', '_'], ['b', 'w', 'b'], ['_', '_', 'w']] or board == [['_', '_', 'b'], ['b', 'w', 'b'], ['w', '_', '_']]:
            board[0][1] = 'w'
            board[1][1] = '_'
        if board == [['_', '_', 'b'], ['w', 'b', '_'], ['_', 'w', '_']] or board == [['b', '_', '_'], ['_', 'b', 'w'], ['_', 'w', '_']]:
            if board[0][2] == 'b':
                board[0][0] = 'w'
                board[1][0] = '_'
            else:
                board[0][2] = 'w'
                board[1][2] = '_'
        if board == [['b', '_', '_'], ['w', 'w', 'b'], ['_', 'w', '_']] or board == [['_', '_', 'b'], ['b', 'w', 'w'], ['_', 'w', '_']]:
            if not biserW[20] + biserW[21] + biserW[22] - 1 <= 0:
                rndm = randint(0, biserW[20] + biserW[21] + biserW[22] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[1][2] == 'b':
                if rndm < biserW[20]:
                    board[0][0] = 'w'
                    board[1][1] = '_'
                    BisUsedW[20] = True
                elif rndm >= biserW[20] and rndm < biserW[20] + biserW[21]:
                    board[0][1] = 'w'
                    board[1][1] = '_'
                    BisUsedW[21] = True
                elif rndm >= biserW[20] + biserW[21] and rndm < biserW[20] + biserW[21] + biserW[22]:
                    board[1][2] = 'w'
                    board[2][1] = '_'
                    BisUsedW[22] = True
            else:
                if rndm < biserW[20]:
                    board[0][2] = 'w'
                    board[1][1] = '_'
                    BisUsedW[20] = True
                elif rndm >= biserW[20] and rndm < biserW[20] + biserW[21]:
                    board[0][1] = 'w'
                    board[1][1] = '_'
                    BisUsedW[21] = True
                elif rndm >= biserW[20] + biserW[21] and rndm < biserW[20] + biserW[21] + biserW[22]:
                    board[1][0] = 'w'
                    board[2][1] = '_'
                    BisUsedW[22] = True
        if board == [['_', 'b', '_'], ['w', 'b', 'b'], ['_', '_', 'w']] or board == [['_', 'b', '_'], ['b', 'b', 'w'], ['w', '_', '_']]:
            if not biserW[23] + biserW[24] + biserW[25] - 1 <= 0:
                rndm = randint(0, biserW[23] + biserW[24] + biserW[25] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[1][2] == 'b':
                if rndm < biserW[23]:
                    board[0][0] = 'w'
                    board[1][0] = '_'
                    BisUsedW[23] = True
                elif rndm >= biserW[23] and rndm < biserW[23] + biserW[24]:
                    board[0][1] = 'w'
                    board[1][0] = '_'
                    BisUsedW[24] = True
                elif rndm >= biserW[23] + biserW[24] and rndm < biserW[23] + biserW[24] + biserW[25]:
                    board[1][1] = 'w'
                    board[2][2] = '_'
                    BisUsedW[25] = True
            else:
                if rndm < biserW[23]:
                    board[0][2] = 'w'
                    board[1][2] = '_'
                    BisUsedW[23] = True
                elif rndm >= biserW[23] and rndm < biserW[23] + biserW[24]:
                    board[0][1] = 'w'
                    board[1][2] = '_'
                    BisUsedW[24] = True
                elif rndm >= biserW[23] + biserW[24] and rndm < biserW[23] + biserW[24] + biserW[25]:
                    board[1][1] = 'w'
                    board[2][0] = '_'
                    BisUsedW[25] = True
        if board == [['b', '_', '_'], ['b', 'w', 'b'], ['_', '_', 'w']] or board == [['_', '_', 'b'], ['b', 'w', 'b'], ['w', '_', '_']]:
            if not biserW[26] + biserW[27] - 1 <= 0:
                rndm = randint(0, biserW[26] + biserW[27] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[2][2] == 'w':
                if rndm < biserW[26]:
                    board[0][0] = 'w'
                    board[1][1] = '_'
                    BisUsedW[26] = True
                elif rndm >= biserW[26] and rndm < biserW[26] + biserW[27]:
                    board[0][1] = 'w'
                    board[1][1] = '_'
                    BisUsedW[27] = True
            else:
                if rndm < biserW[26]:
                    board[0][2] = 'w'
                    board[1][1] = '_'
                    BisUsedW[26] = True
                elif rndm >= biserW[26] and rndm < biserW[26] + biserW[27]:
                    board[0][1] = 'w'
                    board[1][1] = '_'
                    BisUsedW[27] = True
        if board == [['b', '_', '_'], ['b', '_', 'w'], ['_', '_', 'w']] or board == [['_', '_', 'b'], ['w', '_', 'b'], ['w', '_', '_']]:
            if board[1][2] == 'w':
                board[0][2] = 'w'
                board[1][2] = '_'
            else:
                board[0][0] = 'w'
                board[1][0] = '_'
        if board == [['b', '_', '_'], ['w', 'b', 'w'], ['_', '_', 'w']] or board == [['_', '_', 'b'], ['b', 'w', 'b'], ['w', '_', '_']]:
            if not biserW[28] + biserW[29] - 1 <= 0:
                rndm = randint(0, biserW[28] + biserW[29] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[2][2] == 'w':
                if rndm < biserW[28]:
                    board[0][2] = 'w'
                    board[1][2] = '_'
                    BisUsedW[28] = True
                elif rndm >= biserW[28] and rndm < biserW[28] + biserW[29]:
                    board[1][1] = 'w'
                    board[2][2] = '_'
                    BisUsedW[29] = True
            else:
                if rndm < biserW[28]:
                    board[0][0] = 'w'
                    board[1][0] = '_'
                    BisUsedW[28] = True
                elif rndm >= biserW[28] and rndm < biserW[28] + biserW[29]:
                    board[1][1] = 'w'
                    board[2][0] = '_'
                    BisUsedW[29] = True
        if board == [['_', 'b', '_'], ['_', 'b', '_'], ['_', '_', 'w']] or board == [['_', 'b', '_'], ['_', 'b', '_'], ['w', '_', '_']]:
            if not biserW[30] + biserW[31] - 1 <= 0:
                rndm = randint(0, biserW[30] + biserW[31] - 1)
            else:
                print('AI surrenders')
                wb = True
                print()
            if  board[2][2] == 'w':
                if rndm < biserW[30]:
                    board[1][1] = 'w'
                    board[2][2] = '_'
                    BisUsedW[30] = True
                elif rndm >= biserW[30] and rndm < biserW[30] + biserW[31]:
                    board[1][2] = 'w'
                    board[2][2] = '_'
                    BisUsedW[31] = True
            else:
                if rndm < biserW[30]:
                    board[1][1] = 'w'
                    board[2][0] = '_'
                    BisUsedW[30] = True
                elif rndm >= biserW[30] and rndm < biserW[30] + biserW[31]:
                    board[1][0] = 'w'
                    board[2][0] = '_'
                    BisUsedW[31] = True
        if board == [['_', 'b', '_'], ['_', 'w', 'b'], ['w', '_', '_']] or board == [['_', 'b', '_'], ['b', 'w', '_'], ['_', '_', 'w']]:
            if board[1][2] == 'b':
                board[1][0] = 'w'
                board[2][0] = '_'
            else:
                board[1][2] = 'w'
                board[2][2] = '_'
    else:
        if board[1] == ['w', 'b', 'w']:
            if randint(0, 1) == 0:
                board[0][0] = 'w'
                board[1][0] = '_'
            else:
                board[0][2] = 'w'
                board[1][2] = '_'
        if board[1] == ['b', 'w', 'b']:
            board[0][1] = 'w'
            board[1][1] = '_'
    for line in board: print(*line)
    print()
    return wb, board, BisUsedW
#%%
