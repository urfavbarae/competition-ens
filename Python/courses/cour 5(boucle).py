######################################################################################
#Algorithm Pour
######################################################################################
'''
boucle pour: 
<<pour xxxx allant de xx a xxxxxx pas 
instruction 
finpour>>
exemple:
pour i allant de 0 a 4 pas 1
    ecrire("ecrire votre nom complet")
finpour
exemple 2:
pour i allant de 0 a 4 pas 1
    ecrire("entrez un nombre")
    lire(a)
finpour
'''
###########################################################################################
"""
algorithme_tableau_multiplication
variable 
    i : entier
    n : reel
debut
ecrire("saisir un nombre")
lire (n)
pour i allant de 1 a 10 
    ecrire(n,"x",i,"=",n*i)
finpour 
fin
"""
###########################################################################################
"""
algorithme + +
variable 
    n , i , a : entier 
debut 
ecrire("saisir un nombre") 
lire (n)
a <- 0
pour i allant de 1 a n 
    a <- i+a
finpour
ecrire ("la somme est ", a)
fin
"""
###########################################################################################
"""
algorithme factoriel
variable 
    n , i , a : entier
debut 
ecrire("saisir un nombre")
lire (n)
a <- 1
pour i allant de 1 a n 
    a <- i*a
finpour
ecrire("le factoriel est", a)
fin
"""
###########################################################################################
"""
nombre = int(input("Entrez un nombre : "))
if nombre < 0:
    print("Le factoriel n'est pas défini pour les nombres négatifs.")
else:
    resultat = 1
    for i in range(1, nombre + 1):
        resultat *= i
    if nombre == 0:
        resultat = 1
    print(f"Le factoriel de {nombre} est {resultat}.")
"""
###########################################################################################
"""
algorithme 
variable
    i, pos : entier
    max , n : reel
debut
ecrire("saisire nombre numero 1 : ")
lire(n)
max <- n
pos <- 1
pour i allant de 2 a 10
    ecrire("saisire nombre numero",i," : ")
    lire (n)
    si n>=max alors
        max<-n
        pos<-i
    finsi
finpour
ecrire("le nombre maximal est : ",max,"sa position est",pos)
fin
    """
######################################################################################
#Algorithm tant que
######################################################################################
"""
tantque xxxxxx alors 
    xxxxxxxxxxxx
fintantque
"""
#######################################################################################
"""
algorithme 
variable 
    n , max : reel 
    i , pos : entier
debut
ecrire("saisir le nombre numero 1":")
lire(n)
max <- n
pos <- 1
i<-2
tantque n<>0 alors
    ecrire("saisir le nombre numero",i,":")
    lire(n)
    si n<>0 et n>max alors 
        max<-n
        pos<-i
    finsi
    i<-i+1
fintant
ecrire("le nombre maximal est : ",max,"sa position est",pos)
fin
"""
####################################################################
#boucle repeter jusqu'a
####################################################################
"""
repeter 
    instruction
jusqua condition
ex
variable 
    a,b : reel
repeter
    ecrire("saisir a et b")
    lire(a,b)
jusqu'a b<>0
ecrire("la division est ",a/b)
"""
"""
variable 
    n , max : reel
    i , pos : entier
debut 
i<-1
repeter 
    ecrire("saisir le nombre numero" ,i)
    lire (n)
    si n>max ou i=1 alors
        max<-n
        pos<-i
    finsi
    i<-i+1
jusqu'a i>=10
ecrire ("le nombre maximal est : ",max,"sa position est : ",pos)
    
"""
"""n=float(input("saisir le nombre numero 1 : "))
max =n
pos =1
i=2
while n!=0 :
    n=float(input(f"saisir le nombre numero {i} : "))
    if n!=0 and n>max : 
        max=n
        pos=i
    i=i+1
print(f"le nombre maximal est : {max} sa position est : {pos}")"""
####for i in string :#####
email=input("saisir votre e-mail")
for i in email:
    print(i)