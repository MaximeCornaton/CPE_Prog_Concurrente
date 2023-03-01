#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  2 13:45:04 2022

@author: maxime.cornaton
"""

import os,sys

for i in range(3):
    ppid = os.getpid()
    oui = os.fork()
    print("i: ",i," je suis le processus : ", os.getpid(), ", mon père est : ", ppid, "retour : ", oui)
    
sys.exit(0)