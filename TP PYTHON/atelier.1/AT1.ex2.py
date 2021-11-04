#un programme convert les nombres de types a vers type b (decimal >> binaire )
def convert(x):
    if x==0:
        return 0
    else:
        return (x%2)+(10*convert(x//2))
n = int(input("saisir le nbr : "))
print(convert(n))
