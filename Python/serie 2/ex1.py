num=int(input("saisir un nombre : "))
a=0 
for i in range(2,num):
    if num%i==0:
        a+=1
if a==0 and num!=1 and num!=0:
    print(f"le nombre {num} est premier")
else:
    print(f"le nombre {num} n'est pas premier")
print("les nombre premier under 100 sont:")
car=""
b=0
for i in range(2,101): 
    c=i
    for i in range(2,c):
        if c%i==0:
            b+=1
    if b==0:
        car=car+str(c)+","
    b=0
print(car)
print("les 100 premier premier nombre sont : ")
car2=""
f2=0
b2=0
c2=2
while f2<=100 :
    for i in range(2,c2):
        if c2%i==0:
            b2+=1
    if b2==0:
        car2=car2+str(c2)+","
        f2+=1
    b2=0
    c2+=1
print(car2)

"""
algorithme
variable
    num,a,b,i,f,h,f2,i2,c2,b2:reel
debut
ecrire("saisir un nombre: ")
lire(num)
a<-0
si nb=0 ou nb=1 alors
    ecrire(nb,"est non premier")
sinon 
    si nb=2 alors
        ecrire(nb,"est premier")
    sinon    
        pour i allant de 2 a num-1
            si num%i=0 alors
                a<-a+1
            finsi
        finpour
        si a=0 et num<>1 alors
            ecrire("le nombre" ,num,"est premier")
        sinon
            ecrire("le nombre" ,num,"n'est pas premier")
        finsi
    finsi
finsi
ecrire("les nombre premier under 100 sont:")
b=0
pour f allant de 2 a 100
    c=f
    pour h allant de 2 a c-1
        si c%h==0 alors
            b<-b+1
        finsi
    finpour
    si b==0 alors
        ecrire(c)
    finsi
finpour
fin
ecrire("les 100 premier nombre premier sont:")

"""