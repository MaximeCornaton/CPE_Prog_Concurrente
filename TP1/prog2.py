#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:23:18 2022

@author: maxime.cornaton
"""


import os,sys
N = 10
i=1

for j in range(i,N):
    pidpere = os.getpid()
    print("PID DU PERE", pidpere)

    if os.fork() == 0:
        pidfils = os.getpid()
        print("PID DU FILS", pidfils)
        sys.exit(0)

sys.exit(0)