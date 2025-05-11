#ex1:
#algorithme:
"""
algorithme adn
variable
    fonction estadn(mots:chaine de caractaire):boolean
        constant 
            a <-"A"
            c <- "C"
            g <- "G"
            t <- "T"    
        variable first4car : chaine
        debut 
            first4car <- SSCHAINE(mots,0,4)
            si a in first4car et c in first4car et g in first4car et t in first4car alors 
                return true
            sinon 
                return false
            finsi
        fin 
    finfonction
    mot: chaine
debut 
ecrire("saisir le mot que tu veux tester : ")
lire(mot)
ecrire(estadn(mot))
fin
"""

#ex2:
"""
algorithme suit
variable
    fonction fact(n:entier):entier
        variable f , i:entier
        debut
        f<-1
        pour i allant de 1 a n 
            f<-f*i
        finpour
        return f
        fin
    finfonction
    fonction suit(v:entier): reel 
        debut
        si v=0 alors 
            return -1
        sinon
            si v=1 alors
                return 1
            sinon 
                return fact(n)*((1/2)*suit(n-1)+(3/4)*suit(n-2))
            finsi
        finsi
        fin
    finfonction
    i,n :entier
debut
repeter
    ecrire("saisir n")
    lire(n)
jusqu'a n>=0
pour i allant de 0 a n
    ecrire(suit(i))
finpour
fin
"""

