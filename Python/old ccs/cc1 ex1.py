a,b=int(input("entrez a et b Nb: a doit etre inferieur de b : ")),int(input())
while a>b:
    b=int(input("entrez b Nb: a doit etre inferieur de b : "))
c=1
char=""
for i in range(a,b+1):
    c=c*i**2
    if i==a:
        char=str(i)+"^2"
    else:
        char=char+"x"+str(i)+"^2"
print("le prodiut carre total est : ", char ,"=",c)

"""
algorithme
variable 
    a,b,i,c: entier
debut
ecrire("entrer a et b : ")
lire(a,b)
tantque a>b alors 
    ecrire("entrez b Nb: a doit etre inferieur de b : ")
    lire(b)
fintantque
c<-1
pour i allant de a a b 
    c<-c*i^2
finpour
ecrire("le prodiut carre total est : ",c)
fin
"""