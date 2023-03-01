#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 14:21:51 2022

@author: maxime.cornaton
"""

import os,sys
N = 10
i=1
while os.fork()==0 and i<=N :
    i += 1
print(i)
sys.exit(0)