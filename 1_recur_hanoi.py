#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move_hanoi(n,A,B,C):
    if n==1:
        print(f'move {A} to {C} by using {B}')
    else:
        move_hanoi(n-1,A,C,B)
        move_hanoi(1,A,B,C)
        move_hanoi(n-1,B,A,C)

move_hanoi(10,'a','b','c')
