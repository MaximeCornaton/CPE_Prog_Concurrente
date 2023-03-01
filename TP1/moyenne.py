#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 13:58:18 2022

@author: maxime.cornaton
"""

import sys

somme = 0
error = ""

if len(sys.argv[1:]) >=1:
    for arg in sys.argv[1:]:
        if arg.replace('.', '', 1).isdigit() and 0<= float(arg)<= 20 :
            somme += float(arg)
        else:   
            error = "Note(s) non valide(s)"
else:
    error = "Aucune moyenne à calculer"
    
    
if error != "":
    print(error)
else:
    moyenne = somme/len(sys.argv[1:])
    print("Moyenne =", float(str(round(moyenne,3))[0:-1]))
    """print("Moyenne =", "%.2f" %moyenne)"""