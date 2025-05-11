pas=input("entre the password : ")
i=2 
while pas!="hello" and i>0:
    pas=input(f"password wrong retype it (you have {i} chances left ) : ")
    i-=1
if pas=="hello":
    print("login successfully")
else:
    wor=input("write the secret question answer : ")
    if wor=="Minou":
        print("login successfully")
    else:
        print("login denied")

"""
algorithme
variable
    pas , wor : chaine
    i : entier
Debut
Ecrire("entrer le code pin : ")
lire(pas)
i<-2
tantque pas<>"hello" and i>0 alors
    ecrire("code pin incorrect tu as ",i,"chance : ")
    lire(pas)
    i<-i-1
fintantque
si pas="Bonjour" alors
    ecrire("login successfully")
sinon
    ecrire("saisir le message secret")
    lire(wor)
    si wor="Minou" alors
        ecrire("login successfully")
    sinon
        ecrire("login denied")
    finsi
finsi
fin
 """