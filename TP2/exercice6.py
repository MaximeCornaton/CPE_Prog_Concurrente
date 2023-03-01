#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 15:02:53 2022

@author: maxime.cornaton
"""

import os, time, random, sys

for i in range(4) :
    if os.fork() != 0 :
        break
random.seed()
delai = random.randint(0,4)
time.sleep(delai)

try:
    os.wait()
except : sys.exit(1) 

print("Mon nom est " + chr(ord('A')+i) + " j ai dormi " + str(delai) + " secondes")
sys.exit(0)