#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:22:12 2022

@author: maxime.cornaton
"""
import os,sys

for i in range(4) :
    pid = os.fork()
    if pid != 0 :
        print("Ok !")
    print("Bonjour !")
sys.exit(0)