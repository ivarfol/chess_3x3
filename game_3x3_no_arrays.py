#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 13:46:14 2024

@author: iaroslav
"""
wh_turn = ''
wh_alive_list = [True, True, True]
wh_position = ['1:3', '2:3', '3:3']
wh_win = False
wh_win_set = {'1:1', '2:1', '3:1'}
bl_turn = ''
bl_alive_list = [True, True, True]
bl_position = ['1:1', '2:1', '3:1']
bl_win = False
bl_win_set = {'1:3', '2:3', '3:3'}
rturn = 0
coordinats = ('1:1', '1:2', '1:3', '2:1', '2:2', '2:3', '3:1', '3:2', '3:3')
rndm = 0

def validation(turn, coord, position0, position1, col):
    if col:
        direction = -1
    else:
        direction = 1
    return(turn[4:] in coord and turn[:3] in position0 and ((int(turn[2]) + direction == int(turn[6]) and int(turn[0]) == int(turn[4]) and turn[4:] not in position1) or ((int(turn[2]) - 1 == int(turn[6]) or int(turn[2]) + 1 == int(turn[6])) and (turn[4:] in position1) and (int(turn[0]) - 1 == int(turn[4]) or int(turn[0]) + 1 == int(turn[4])))))

def NowherToGo(coord, position0, position1, col):
    flag = True
    for i in position0:
        for j in coord:
            if i != j:
                if validation( i + '.' + j, coord, position0, position1, col):
                    flag = False
                    break
        if not flag:
            break
    return(flag)

while not(wh_win or bl_win): #game end
    rturn += 1
    wh_turn = input(f'turn {rturn}\nWhite turn\nx:y.x:y\n')
    while not(validation(wh_turn, coordinats, wh_position, bl_position, True)):
        wh_turn = input('\nproper coordinats required\nx:y.x:y\n')
    for i in range(3):
        if wh_turn[:3] == wh_position[i]:
            wh_position[i] = wh_turn[4:]
        if bl_position[i] in wh_position:
            bl_position[i] = '0:0'
            bl_alive_list[i] = False
        if wh_position[i] in wh_win_set or (bl_alive_list[0] == False and bl_alive_list[1] == False and bl_alive_list[2] == False) or NowherToGo(coordinats, bl_position, wh_position, False):
            wh_win = True
    print(*wh_position)
    print(*bl_position)
    if wh_win == True:
        break
    
    rturn += 1
    bl_turn = input(f'turn {rturn}\nBlack turn\nx:y.x:y\n')
    while not(validation(bl_turn, coordinats, bl_position, wh_position, False)):
        bl_turn = input('\nproper coordinats required\nx:y.x:y\n')
    for j in range(3):
        if bl_turn[:3] == bl_position[j]:
            bl_position[j] = bl_turn[4:]
        if wh_position[j] in bl_position:
            wh_position[j] = '0:0'
            wh_alive_list[j] = False
        if bl_position[j] in bl_win_set or (wh_alive_list[0] == False and wh_alive_list[1] == False and wh_alive_list[2] == False) or NowherToGo(coordinats, wh_position, bl_position, True):
            bl_win = True
    print(*wh_position)
    print(*bl_position)
if wh_win:
    print('Whites win')
else:
    print('Blacks win')