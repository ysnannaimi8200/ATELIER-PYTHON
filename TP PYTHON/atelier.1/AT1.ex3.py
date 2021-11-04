def somme(n):
    if n==0:
        return 0
    else:
        return n + somme(n-1)
n = int(input("saisir le nbr de sommet : "))
print(somme(n))
# un script qui calcule la somme par la récursivité
