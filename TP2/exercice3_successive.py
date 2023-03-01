#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:49:00 2022

@author: benjamin.sayaque
"""

import os, sys
if os.fork() != 0:
    os.wait()
    if os.fork() != 0:
        os.wait()
        os.execlp("ls", "ls", "-l")
        sys.exit(0)
    else:
        os.execlp("ps", "ps")
else:
    os.execlp("who", "who")
sys.exit(1)