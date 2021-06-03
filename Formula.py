# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 14:22:56 2021

@author: Windows 10 Pro
"""

import math

def Circle(r):
    S = math.pi * (r ** 2)
    return S

def Circle_1(r):
    C = 2 * math.pi * r
    return C
def Square_Circle(r):
    P = 8 * r
    return P

def Sector(s,r):
    S1 = (s*r)/2
    return S1
