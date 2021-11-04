# programme compte l'occurrence de chaque élément et montrer le nombre de chaque élément 
def occur(list1):
    x = {}
    for i in list1:
        if str(i) in x:
            x[str(i)] = x.get(str(i)) + 1
        else:
            x[str(i)] = 1
    return x

print(occur([1,2,2,2,3,4,5,77,77,65,43]))