def select(list1,dictA):
    keys = list(dictA.keys())
    resultat = []
    for i in keys:
        for j in list1:
            if dictA[str(i)] == j :
                resultat.append(j)
    return resultat
print(select([47,64,69,37,76,83,95,97],
{'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}))