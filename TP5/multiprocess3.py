#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:18:22 2022

@author: maxime.cornaton
"""

import multiprocessing as mp
def maFonction(num) :
    moi = mp.current_process()
    print("Bonjour", num, moi.pid , moi._parent_pid)
if __name__ == "__main__" :
    listeP = [ ]
    for i in range(5) :
        p = mp.Process(target = maFonction, args=( i, ))
        listeP.append(p)
        p.start()
    for p in listeP :
        p.join()    