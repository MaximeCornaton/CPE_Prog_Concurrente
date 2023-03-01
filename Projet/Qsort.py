# Mai 2022
# qsort très court

import random
import multiprocessing as mp


def q_sort(Liste) :
    #Pivot = Liste[0]
    if len(Liste) > 1 :
        Pivot = Liste[0]
        gauche =  q_sort([x for x in Liste[1:] if x <= Pivot])
        droite = q_sort([x for x in Liste[1:]  if x > Pivot])
        
        return gauche + [Pivot] + droite
    return Liste

def Process(taille_liste, nb_process):
    mes_process = [0 for i in range(nb_process)]

    for i in range(nb_process):
        mes_process[i] = mp.Process(target=q_sort, args= ())
        mes_process[i].start()

    for i in range(nb_process): mes_process[i].join()

    return 


if __name__ == "__main__" :
    nb_process = 8
    lst=[random.randint(10,100) for _ in range(10)]
    print("Avant : ", lst)
    print("Après : ", q_sort(lst))
