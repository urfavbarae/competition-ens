n=int(input("entrez la premier valeur du suit (n>1): "))
i=0
while n<=1 :
    n=int(input("entrez la premier valeur du suit (n>1) : "))
while n!=1:
    if n%2==0:
        n=n/2
        print(f"u{i}={n}")
    else:
        n=n*3+1
        print(f"u{i}={n}")
    i+=1

"""
algorithme
variable
    n,i : reel
debut
ecrire("entrez la premier valeur du suit (n>1):")
lire(n)
tantque n<=1 alors
   ecrire("entrez la premier valeur du suit (n>1):")
   lire(n) 
fintantque
i<-0
tantque n<>1 alors
    si n%2=0 alors
        n<-n/2
        ecrire("u",i,"=",n)
    sinon
        n<-n*3+1
        ecrire("u",i,"=",n)
    finsi
    i<-i+1
fintantque
fin

"""