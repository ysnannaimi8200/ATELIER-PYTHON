#fonction pour deiviser une lsite en 3 morceau egaux
#division de la liste sur 3, en assurant que n soit interger pour lutiliser apres
#declaration de la 1ere ,2eme et 3eme list
def diviser(TAB):
    x = len(TAB)
    x = int(x/3)
    listA = []
    listA = TAB[0:x]
    listA.reverse()
    print(listA)
    listB = []
    listB = TAB[x:-x]
    listB.reverse()
    print(listB)
    listC = []
    listC = TAB[-x:]
    listC.reverse()
    print(listC)


LIST= [12,34,87,61,90,4,56,77,32,7,58,91]
print(diviser(LIST))