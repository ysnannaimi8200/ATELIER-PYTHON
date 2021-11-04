#un programme en Python pour trouver la somme des séries
def factoriel(x):
   if x==1 :
      return 1
   else :
       return(x*factoriel(x-1))
n=5
s=0
for i in range(1,n+1) :
    s=s+factoriel(i)/i
    print(s)