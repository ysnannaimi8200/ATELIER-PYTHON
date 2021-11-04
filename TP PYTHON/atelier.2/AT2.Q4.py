'''la fct commun est pour afficher les nbrs repeter dans les
deux set et de suprimer les nombre non repeter au 1er set '''
def commun(set1, set2):
    x = set((""))
    for i in set1:
        for j in set2: 
            if i == j: x.add(i)
    y = set1.copy()
    for i in set1:
        if i in x: y.remove(i)

    print("les nbrs commun sont : ", x)
    print("les nombres suprime sont :", y)

print(commun({21,11,56,87,44,90}, {11,33,87,90}))
