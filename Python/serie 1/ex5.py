va=int(input("saisir la valeur a rechercher : "))
a=0 
for i in range(1,11):
    num=int(input("saisir le {i} nombre :"))
    if num==va :
        a+=1
print(f"la valeur à rechercher apparait {a} fois")

"""
algorithme 
variable
    va,a : reel
debut 
ecrire("saisir la valeur a rechercher : ")
lire(var)
a<-0
pour i allant de 1 a 10
    ecrire("saisir le" ,i, "nombre :")
    lire(num)
    si num=va alors
        a<-a+1
    finsi
finpour
ecrire("la valeur à rechercher apparait" ,a ,"fois")
"""