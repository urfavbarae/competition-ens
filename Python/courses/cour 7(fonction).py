####les fcts algo####
"""
la fonction est un code qui fait un traitement et qu'on lui attribue un nom et des parametres 
- il y a deux type des fct: 1. une fct qui retourne un resultat 
                            2. une fct qui fait un traitement sans retourner un resultat: (procedure)
"""
####definition des fonction on algo####
"""
algorithme
variable
    Fonction surface(r:reel) : reel
        constante pi=3.14
        variable s: reel
        debut
        S<-Pi*r^2
        retourne S
    finfonction
    X,a:reel
debut
ecrire("entrez le rayon : ")
lire(x)
ecrire("l surface de cercle est: ",surface(x))
ecrire("la surface de mon cercle ",surface(5.9))
a<-surface(1)
fin
"""
"""
algorithme
variable
    Fonction somme (a,b:reel) : reel
        variable:
            s:reel
        debut
        s<-a+b
        retourne s
        fin
    fin fonction
    x,y:reel
debut 
ecrire ("Saisir a et b" )
lire(x,y)
ecrire("la somme est: ",somme(x,y))
"""
"""
algorithme
Variable
    fonction facto(nb:entier):entier
        variable i, p:entier
        debut
        si nb=0 alors
            p<-1
        sinon
            p<-1
            pour i allant de 1 a nb 
                p<-p*i
            finpour
        finsi
        retourne p
    finfonction 
    x:entier
debut
repeter 
    ecrire("entrez un nombre positif")
    lire(x)
jusqua x>=0
Ecrire(" le factoriel de ",x "est :",Facto(x))
"""