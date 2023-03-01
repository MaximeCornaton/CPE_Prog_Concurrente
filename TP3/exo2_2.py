#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  9 15:14:17 2022

@author: maxime.cornaton
"""



import os , sys 
fichier=sys.argv[1]

(dfr,dfw) = os.pipe( ) 

pid = os.fork()

if pid != 0 :
    os.close(dfr) # ferme la sortie du tube
    os.write(dfw,fichier)
    
    os.close(dfw) # ferme le descripteur de l’entrée du tube
     
    
else :
    os.close(dfw) # ferme l’entrée du tube
    os.dup2(dfr , 0) # copie la sortie du tube vers l’entrée standard (clavier)
    os.close(dfr) # ferme le descripteur de la sortie du tube
    os.execlp("grep","grep", "chaine") 
    

sys.exit(0)