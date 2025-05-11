ch=0
a=None
b=None
while ch!=3:
    ch=int(input("""1. entrez a et b:
2. affichez le produit des nombre entre a et b
3. Quitter

votre choix : """))   
          
    if ch==1:
        a=int(input("saisir a : "))
        b=int(input("saisir b : "))
        while b<=a:
            b=int(input("saisir b (b>a): "))
    elif ch ==2:
        if a==None and b==None:
            print("tu n'a pas saisie a et b revien au menue et resaisie le")
        else :
            so=1
            for i in range(a+1,b):
                so*=i
            print("la somme entre a et b est : ",so)
    elif ch==3:
        print("merci")
    else:
        print("choix unvalid")
"""
Algorithme
Variable 
    ch,a,b,so,i:reel
debut
ch<-0
a<-0
b<- -2
tantque
    ecrire("1. entrez a et b:")
    ecrire("2. affichez le produit des nombre entre a et b")
    ecrire("3. Quitter")
    ecrire("")
    ecrire("votre choix :")
    lire(ch)
    si ch=1:
        
"""

    