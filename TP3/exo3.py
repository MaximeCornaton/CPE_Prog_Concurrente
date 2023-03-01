#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 17:07:35 2022

@author: maxime.cornaton
"""

import os , sys, random # Communication par tube anonyme os.pipe()

N = 10
(dfrPAIRE,dfwPAIRE) = os.pipe() # NOMBRES PAIRS
(dfrIMP,dfwIMP) = os.pipe() # NOMBRES IMPAIRS

(dfrSPAIRE,dfwSPAIRE) = os.pipe() # SOMME PAIRS
(dfrSIMP,dfwSIMP) = os.pipe() # SOMME IMPAIRS

pid = os.fork()


if pid != 0 : #Processus Père / GENERATEUR
    os.close(dfrPAIRE)
    os.close(dfrIMP)
    
    for i in range(N):
        nbr = random.randint(0,999999999)%2
        if nbr == 0:
            os.write(dfwPAIRE , str(nbr).encode())
        else:
            os.write(dfwIMP, str(nbr).encode())
        
    os.write(dfwPAIRE , "-1".encode())
    os.write(dfwIMP , "-1".encode())

    os.close(dfwPAIRE)
    os.close(dfwIMP)
    
    os.close(dfwSPAIRE)
    os.close(dfwSIMP)
    
    nbr1 = os.read(dfrSPAIRE , len(nbr)).decode()
    nbr2= os.read(dfrSIMP , len(nbr)).decode()
    
    print(int(nbr1)+int(nbr2))
    
    os.close(dfrSPAIRE)
    os.close(dfrSIMP)
    
else : #Processus fils

    
    # os.close(dfw)
    # msgReception = os.read(dfr , len(msg)).decode()
    # n = len(msgReception)
    # print ("Le processus %d:%d octets, message recu est %s \n" %(os.getpid(), n, msgReception))
    # os.close(dfr)
    
sys.exit(0)