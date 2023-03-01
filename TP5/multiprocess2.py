#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 16 14:15:35 2022

@author: maxime.cornaton
"""

import multiprocessing as mp
def fonctionAffichage(continent = "Asie") :
    print("Le nom du continent = ", continent)
    
if __name__ == "__main__" :
    listeContinents = ["Amérique" , "Europe", "Afrique"]
    listeProcess = [ ]
    process = mp.Process(target = fonctionAffichage)
    listeProcess.append(process)
    process.start()
    for nom in listeContinents :
        process = mp.Process(target = fonctionAffichage, args=(nom,))
        listeProcess.append(process)
        process.start()
    for p in listeProcess :
        p.join()