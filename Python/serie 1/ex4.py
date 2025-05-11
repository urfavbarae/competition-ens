import random
num=int(input("guess a number from 1 to 100: "))
while num<1 or num>100:
    num=int(input("i said from 1 to 100: "))
c=random.randint(1, 100)
while num!=c and num!=0:
    while num<0 or num>100:
        num=int(input("i said from 1 to 100: "))
    if num>c :
        num=int(input("le nombre est plus grand (try again) or tape 0 to know the answer: "))
    else:
        num=int(input("le nombre est plus petit (try again) or tape 0 to know the answer: "))
if num==0:
    print(f"nice try the number is ({c}) good luck next time")
else:
    print(f"congratulations the number is correct ({c})")

"""
algorithme 
variable
    num,c :entier
debut
ecrire("guess a number from 1 to 100: ")
lire(num)
tantque num<1 ou num>100 alors
    ecrire("i said from 1 to 100: ")
    lire(num)
fintantque
c=63
tantque num<>c et num<>0 alors
    tantque num<1 ou num>100 alors
        ecrire("i said from 1 to 100: ")
        lire(num)
    fintantque
    si num>c alors
        ecrire("le nombre est plus grand (try again) or tape 0 to know the answer: ")
        lire(num)
    sinon
        ecrire("le nombre est plus petit (try again) or tape 0 to know the answer: ")
        lire(num)
    finsi
finsi
si num=0 alors
    ecrire ("nice try the number is" ,c, " good luck next time")
sinon
    ecrire("congratulations the number is correct (",c,")" )
finsi
fin
"""