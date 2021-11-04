#programme qui compte le nbr des chifres a base de principe de recursivite
def fonction(x):
    if x < 10:
        return 1
    else :
        return 1 + fonction(x//10)
x = int(input("saisir un nbr : " ))
print("ce nbr ",x,"contient ",fonction(x),"chiffre")
