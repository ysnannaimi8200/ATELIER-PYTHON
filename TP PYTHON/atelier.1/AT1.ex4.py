#programme qui traite la serie de fibonacci
def fibonacci(n):
    if(n<=0):
        return 1
    else :
        return(fibonacci(n-1)+fibonacci(n-2))
n = int(input("saisir le nbr : "))
print("le nbr est :  ",n)
for i in range(n):
    print("la serie de Fibonacci est : ",fibonacci(i))