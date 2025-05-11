""" dtest={"p1_563": ["lait",12.3,14,63], "p2_897": ["yaourt",2.3,3,200], "p3_578": ["jus",5,6.3,80]} """

def remp(d):
    n=int(input("saisir le nombre de produit : "))
    for i in range(1,n+1):
        code=input("saisir le code du produit : ")
        d[code]=[input("saisir le nom de produit : "),float(input("saisir le prix d'achat : ")),float(input("saisir le prix de vente : ")),int(input("saisir le quantite en stock : "))]


def existanse(d,code):
    if code in d:
        return True
    else:
        return False

def modif(d,code):
    d[code][0]=input("saisir le nom de produit : ")
    d[code][1]=float(input("saisir le prix d'achat : "))
    d[code][2]=float(input("saisir le prix de vente : "))
    d[code][3]=int(input("saisir le quantite en stock : "))
    return d

def supp(d):
    dc=d.copy()
    for i in dc:
        if dc[i][3]==0:
            d.pop(i)
    return d

def som_prdct(d):
    s=0
    for i in d:
        s+=d[i][3]
    return s

def remp_achat_cl(dc,dp):
    nc=int(input("saisir le nombre de clients : "))
    for i in range(1,nc+1):
        np=int(input("saisir le nombre de produit achete par le client {i} : "))
        for j in range(1,np+1):
            code=input("saisir le code du produit : ")
            if code in dp:
                dc[f"clt{i}"][code]=int(input("saisir la quantite achete : "))
    return dc

def prix_paye(d,d1):
    dt={}
    for i in d1:
        s=0
        for j in d1[i]:
            s+=d1[i][j]*d[j][2]
        dt[i]=s
    return dt

def achat_total(d,d1):
    d2=prix_paye(d,d1)
    return sum(d2.values())

choix=0
d=remp({})
while choix!=7:
    choix=int(input("""
-------------Menu------------- 
1 : Rechercher un produit
2 : Modifier un produit.
3 : Supprimer le produit qui n'existe pas dans le stock.
4 : Afficher la quantité totale.
5 : Afficher les informations de chaque produit.
6 : Enregistrer dans un fichier
7 : Quittez le programme
Tapez votre choix : """))
    if choix==1:
        print(existanse(d,input("saisir le code du produit : ")))
    elif choix==2:
        print(modif(d,input("saisir le code du produit : ")))
    elif choix==3:
        print(supp(d))
    elif choix==4:
        print(som_prdct(d))
    elif choix==5:
        for i in d:
            print(i,d[i],sep=" => ")
    elif choix==6:
        print("service unvalide")
    elif choix==7:
        print("au revoir")
        break
    else:
        print("choix unvalide")
