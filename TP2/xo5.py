#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 16:37:57 2022

@author: maxime.cornaton
"""

import os,time, sys

N = int(sys.argv[1])

for i in range(N) :
    pi = os.fork()
    pid_fils = os.getpid()
    pid_pere = os.getppid()
    time.sleep(2*i)
    pid_fils, etat =os.wait()
    
    print("pid fils: ", pid_fils, "pid père : ", pid_pere, "etat : ", etat)
    
    sys.exit(i)