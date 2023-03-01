#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 13:32:48 2022

@author: maxime.cornaton
"""

import multiprocessing as mp
def fonctionAffichage(num) :
    print("Bonjour", num)
    
if __name__ == "__main__":
    n = 0
    process = mp.Process(target = fonctionAffichage, args=( n, ) )
    process.start()
    process.join()
    print("Process actif ?", process.is_alive()) 