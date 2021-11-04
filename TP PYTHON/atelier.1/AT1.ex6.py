def tri_bull(tab):
    n = len(tab)
    for i in range(n):
        for j in range(0,n-i-1):
            if tab[j] > tab[j+1]:
                tab[j],tab[j+1] = tab[j+1],tab[j]
    return tab
def tri_selection(tab):
    for i in range (len(tab)):
        min = i
        for j in range (i+1 , len(tab)):
            if tab[min] > tab[j]:
                min = j
        tmp = tab[i]
        tab[i] = tab[min]
        tab[min] = tmp
    return tab
def tri_insertion(tab):
    for i in range(1,len(tab)):
        k = tab[i]
        j = i - 1
        while j>=0 and k<tab[j]:
            tab[j+1] = tab[j]
            j=-1
            tab[j+1] = k
    return tab
tab = [20,12,45,89,1,23,54,34,60,99]
print("TRI A BULL : ",tri_bull(tab))
print("TRI PAR SELECTION : ",tri_selection(tab))
print("TRI PAR INSERTION : ",tri_insertion(tab))
