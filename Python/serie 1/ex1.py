x=float(input("saisir la valeur de x : "))
n=int(input("saisir la valeur de n : "))
while n<=0:
    n=int(input("n doit etre negative or null resaisie le : "))
a=0
for i in range(1,n+1):
    a=a+x**i
print(f"sigma de x^n de 1 jusqu'a {n} est : {a}")

"""
algorithme
variable 
    x : reel
    n,a : entier
debut
ecrire("saisir la valeur de x : ")
lire (x)
ecrire("saisir la valeur de n : ")
lire(n)
tantque n<=0 alors
    ecrire("n doit etre negative or null resaisie le : ")
    lire(n)
fintantque
a<-0
pour i allant de 1 a n 
    a<-a+x^i
finpour
ecrire("sigma de x^n de 1 jusqu'a ",n ,"est :",a )
fin
"""