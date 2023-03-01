#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 14:06:40 2022

@author: maxime.cornaton
"""

import os,sys
N = 3
i=1
t = ["who","ps","ls -l"]

for j in range(i,N):
    pidpere = os.getpid()
    print("PID DU PERE", pidpere)

    if os.fork() == 0:
        pidfils = os.getpid()
        print("PID DU FILS", pidfils)

sys.exit(0)
