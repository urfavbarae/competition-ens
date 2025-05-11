a=int(input('entrer le premier nombre : '))
b=int(input('entrer le dexieme nombre : '))
c=int(input('entrer le troisieme nombre : '))
print("""
-------------menu----------------
1.----------moyenne--------------
2.----------maximum--------------
3.----------minimum--------------
---------------------------------
""")
ch=input("choisir le program que tu veux : ")
if ch=="1":
    print("le moyenne est", sum([a,b,c])/3)
elif ch=="2":
    print("la plus petit valeur est:",min(a,b,c))
elif ch=="3":
    print("la plus grand valeur est:",max(a,b,c))
else:
    print("choice unavalible")

"""
algorithme
variable
    a, b, c : reel
    ch : chaine
debut 
ecrire("entrez 3 nombre")
lire(a,b,c)
ecrire("-------------menu----------------")
ecrire("1.----------moyenne--------------")
ecrire("2.----------maximum--------------")
ecrire("3.----------minimum--------------")
ecrire("---------------------------------")
ecrire("saisir ton choix")
lire(ch)
si ch="1" alors
    ecrire("la moyenne est", (a+b+c)/3)
sinon 
    si ch="2" alors
        si a>b et a>c alors
            ecrire("le max est",a)
        sinon 
            si b>a et b>c alors
                ecrire("le max est",b)
            sinon 
                ecrire("le max est",c)
            finsi
        finsi
    sinon 
        si ch="3" alors
            si a<b et a<c alors
                ecrire("le min est",a)
            sinon 
                si b<a et b<c alors
                    ecrire("le min est",b)
                sinon 
                    ecrire("le min est",c)
                finsi
            finsi
        sinon 
            ecrire("categorie unvalid")
        finsi
    finsi
finsi
    

"""