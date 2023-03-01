#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:49:00 2022

@author: benjamin.sayaque
"""

import os, sys

if os.fork() == 0:
    os.execlp("ls", "ls", "-l")

if os.fork() == 0:
    os.execlp("ps", "ps")

os.execlp("who", "who")

