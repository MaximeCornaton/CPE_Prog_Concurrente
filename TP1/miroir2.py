#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:56:14 2022

@author: maxime.cornaton
"""

import sys
oui = []

for arg in sys.argv[1:]:
    oui.append(''.join(reversed(arg)))
    
print(' '.join(oui))