def trouve(str , char):
    return str.count(char)
str1 = input("saisir le string : ")
char1 = input("saisir le char : ")
print("le char ",char1,"repeter ",trouve(str1,char1),"fois")
#la fct trouve la fréquence d’un caractère dans une chaîne