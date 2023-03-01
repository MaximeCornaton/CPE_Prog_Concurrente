#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 16:03:47 2022

@author: benjamin.sayaque
"""

import os, sys
n=0
for i in range(1,5) :
    fils_pid = os.fork() #1
    if (fils_pid > 0) : #2
        os.wait() #3
        n = i*2
        break;
print("n = ", n) #4
sys.exit(0)

# Après la ligne étiquetée #2 on se retrouve dans le procesus père, fils_pid = 0 pour le fils.
# Ce programe est déterministe puisque le père attend à chaque fois que le processus du fils soit terminé avant 
# de continuer. 