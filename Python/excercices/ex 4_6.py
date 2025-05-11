n=float(input("saisir la nbr numero 1 : "))
m=n
i=1 
while n!=0 :
    i+=1
    n=float(input(f"saisir la nbr numero {i} : "))
    m=m+n
i-=1
print(f"la moy des nombres est: {m/i}")
"""
variable 
    n,m : reel 
    i : entier 
debut 
ecrire ("saisire la nombre numero 1:")
lire(n)
m<-n
i<-1
tanque n<>0 alors
    i<-i+1
    ecrire ("saisire la nombre numero",i," : ")
    lire(n)
    m<-m+n
fintanque
i=i-1
ecrire("la moy des nombres est: ", m/i)
fin
    """
"""
variable 
    n,m : reel 
    i : entier 
debut 
i<-1
m<-0
repeter
ecrire ("saisire la nombre numero",i," : ")
lire(n)
m<-m+n
i<-i+1
jusqu'a n=0
i=i-1
ecrire("la moy des nombres est: ", m/i)
fin
"""