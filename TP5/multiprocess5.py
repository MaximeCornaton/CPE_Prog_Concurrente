#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:23:17 2022

@author: maxime.cornaton
"""

import multiprocessing as mp
import sys , time, random

def fonc(l , i) :
    l.acquire()
    for k in range(20) :
        print ("Bonjour ", i)
    l.release()
       
lock = mp.Lock()
for num in range(10) :
    p = mp.Process(target = fonc , args=(lock,num,))
    p.start()