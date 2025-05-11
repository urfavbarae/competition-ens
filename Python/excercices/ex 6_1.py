c=input("entrez une chaine :")
cpn=0
cpl=0 
for i in c:
    if i.isalpha():
        cpl+=1
    elif i.isnumeric():
        cpn+=1
print(f"le nbr de lett est {cpl} , le nbr de chiffre {cpn}")
"""
algorithme 
variable
    i, cpn, cpl, cd :entier
    c :chaine
debut
ecrire("entrez une chaine:")
lire(c)
cpl<-0
cpn<-0
pour i allant de 0 a Longueur(c)-1
    cd<-code(c[i])
    si cd<-65 et cd<-code("z") ou (cd=>97 et cd<=122) alors
        cpl<-cpl+1
    
"""