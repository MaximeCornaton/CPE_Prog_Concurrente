#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:27:17 2022

@author: maxime.cornaton
"""

import os , sys # Communication par tube anonyme os.pipe()
fichier=sys.argv[1]
(dfr,dfw) = os.pipe( ) # création d’un tube
pid = os.fork()
if pid != 0 :
    os.close(dfr) # ferme la sortie du tube
    os.dup2(dfw , 1) # copie l’entrée du tube vers la sortie standard (écran)
    os.close(dfw) # ferme le descripteur de l’entrée du tube
    os.execlp("cat","cat" , fichier) # recouvre avec ls -l
else :
    os.close(dfw) # ferme l’entrée du tube
    os.dup2(dfr , 0) # copie la sortie du tube vers l’entrée standard (clavier)
    os.close(dfr) # ferme le descripteur de la sortie du tube
    os.execlp("wc","wc") # recouvre avec wc –l
sys.exit(0)