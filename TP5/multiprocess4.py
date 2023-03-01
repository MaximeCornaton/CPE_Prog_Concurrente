#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:20:20 2022

@author: maxime.cornaton
"""

import multiprocessing as mp
import sys , time, random

def process1(s) :
    print("Je suis le process 1 et j'attends 15 secondes")
    time.sleep(15)
    print("Je suis le process 1 et je génère un jeton [ V(s) ]")
    s.release()
    sys.exit(0)
    
def process2(s) :
    print("Je suis le process 2 et je me bloque sur le sémaphore : [ P(s) ]")
    s.acquire()
    print("Je suis le process 2 et je suis DEBLOQUE")
    sys.exit(0)
    
sem = mp.Semaphore(0) #Création d'un sémaphore
p1 = mp.Process(target = process1 , args = (sem,))
p2 = mp.Process(target = process2 , args = (sem,))
p1.start()
p2.start()
p1.join()
p2.join()
sys.exit(0)