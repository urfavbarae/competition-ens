num=int(input("saisir un nombre positif : "))
while num<0:
    num=int(input("i said positive not negative : "))
if num==0 or num==1:
    print(f"{num} n'est pas parfait")
else:
    c=0
    for i in range(1,num):
        if num%i==0:
            c=c+i
    if c==num:
        print(f"{num} est un nombre parfait")
    else:
        print(f"{num} n'est pas un nombre parfait")

"""
algorithme
variable 
    num,c,i : entiers
debut
ecrire(" saisir un nombre positif")
lire(num)
tantque num<0 alors
    ecrire("i said positif")
    lire (num)
fintantque
si num=0 ou num=1 alors
    ecrire(num," n'est pas parfait")
sinon
    c<-0
    pour i allant de 1 a num-1
        si num%i=0 alors
            c<-c+i
        finsi
    finpour
    si c=num alors
        ecrire(num,"est un nombre parfait")
    sinon
        ecrire(num,"n'est pas un nombre parfait")
    finsi
finsi
fin
"""