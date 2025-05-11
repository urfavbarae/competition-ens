a,b=int(input("entrez a et b Nb: a doit etre inferieur de b : ")),int(input())
while a>b:
    b=int(input("entrez b Nb: a doit etre inferieur de b : "))
char="("
for i in range(a,b+1):
    if i%2==0:
        char=char+str(i)+","
char+=")"
print(f"les nbr pair entre {a} et {b} sont : {char}")
"""
algorithme
variable
    a,b,i:reel
debut 
ecrire("entrer a et b : )
lire(a,b)
tantque a>b alors
    ecrire("entrez b Nb: a doit etre inferieur de b : ")
    lire(b)
fintantque
ecrire("les nbr pair entre",a,"et",b, "sont :")
pour i allant de a a b
    si i%2=0 alors
        ecrire(i)
    finsi
finpour
fin
"""