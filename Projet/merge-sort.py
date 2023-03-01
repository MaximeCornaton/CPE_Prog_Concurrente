import math, random, time
from array import array
 
def merge(Tableau, start1, start2, j1, j2):
    tab = array('i', [])  # tableau vide qui reçoit les résultats
    i1, i2 = start1, start2
    while i1<j1 and i2<j2:
        if Tableau[i1] < Tableau[i2]:
            tab.append(Tableau[i1])
            i1+=1
        else: 
            tab.append(Tableau[i2])
            i2+=1
    while i1 < j1:
        tab.append(Tableau[i1])
        i1 += 1
    while i2 < j2:
        tab.append(Tableau[i2])
        i2 += 1
    Tableau[start1: j2] = tab
    return tab

def merge_sort(Tableau, i, j):
    if i>=j-1:
        return i
    mid = (j+i) // 2
    print(mid, i, j)
    merge_sort(Tableau, i, mid)
    merge_sort(Tableau, mid, j)
    return merge(Tableau, i, mid, mid, j)

def version_de_base(N):
    Tab = array('i', [random.randint(0, 2 * N) for _ in range(N)]) 
    print("Avant : ", Tab)
    start=time.time()
    Tab = merge_sort(Tab, 0, N)
    end=time.time()
    print("Après : ", Tab)
    print("Le temps avec 1 seul Process = %f pour un tableau de %d eles " % ((end-start)*1000, N))
    
    print("Vérifions que le tri est correct --> ", end='')
    try :
        assert(all([(Tab[i] <= Tab[i+1]) for i in range(N-1)]))
        print("Le tri est OK !")
    except : print(" Le tri n'a pas marché !")

if __name__ == "__main__" :
    version_de_base(10)

