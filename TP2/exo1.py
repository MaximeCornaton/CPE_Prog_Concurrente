#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:37:51 2022

@author: maxime.cornaton
"""

import os,sys


pidpere = os.getpid()
print("PID DU PERE", pidpere)

if os.fork() == 0:
    pidfils = os.getpid()
    print("PID DU FILS", pidfils)
    os.execlp("python", "python", "oui.py")
    sys.exit(0)
    
print("jeanne la mechante")
    
sys.exit(0)