
def remp(n):
    d={}
    for i in range(1,n+1):
        name=input("saisir le nom : ")
        d[name]=int(input("saisir le nombre de ventes : "))
    return d

def somme(d):
    s=0
    for i in d.values():
        s+=i
    return s

""" print(somme(ventes)) """

def max_vent(d):
    max=0
    pmax=""
    for i in d.keys():
        if d[i]>max:
            max=d[i]
            pmax=i
    return pmax

""" print(max_vent(ventes)) """

def sup_min_vente(d):
    min=d[max_vent(d)]
    pmin=""
    for i in d.keys():
        if d[i]<min:
            min=d[i]
            pmin=i
    d.pop(pmin)
    return d
""" print(sup_min_vente(ventes)) """
# methode de get the key of the min 
#min(l,key=l.get)
def sup_min_vente2(d):
    for i in range(list(d.values()).count(min(d,key=d.get))):
        d.pop(min(d,key=d.get))

def sup_someone(d,nom):
    d.pop(nom)
    return d

def sortvl(d):
    l=sorted(d.values())
    ds={}
    for i in l:
        for j in d.keys():
            if d[j]==i:
                ds[j]=i
    return ds
""" print(sortvl(ventes)) """

def modf_vent(d,nom):
    if nom not in d.keys():
        return "ce nom n'existe pas dans le dictionnaire"
    d[nom]=input("saisir la nouvelle valeur : ")
    return d

def find_vent(d,nom):
    if nom not in d.keys():
        return "ce nom n'existe pas dans le dictionnaire"
    return d[nom]

def enregistre_ventre(d):
    f=open(".\\courses\\files\\ventes.txt","a")
    for i in d:
        f.write(f"{i} => {d[i]} \n")
    f.close()
    
choix=-1
D={}
while choix!=10:
    choix=int(input("""
-------------Menu------------- 
1 : Ajouter les ventes.
2 : Afficher les ventes.
3 : Afficher les ventes triées.
4 : Modifier les ventes d'un vendeur .
5 : Rechercher les ventes d'un vendeur .
6 : Supprimer un vendeur.
7 : Afficher le nombre total des ventes.
8 : Afficher le vendeur qui a réalisé plus de vente.
9 : Enregistrer dans un fichier.
10: Quittez le programme.
Tapez votre choix : """))
    if choix==1:
        D=remp(int(input("saisir le nombre de vendeurs : ")))
    elif choix==2:
        if D=={}:
            print("la dictionaire est vide")
        else:
            print(D)
    elif choix==3:
        if D=={}:
            print("la liste est vide")
        else:
            print(sortvl(D))
    elif choix==4:
        if D=={}:
            print("la liste est vide")
        else:
            print(modf_vent(D,input("saisir le nom du vendeur : ")))
    elif choix==5:
        if D=={}:
            print("la liste est vide")
        else:
            print(find_vent(D,input("saisir le nom du vendeur : ")))
    elif choix==6:
        if D=={}:
            print("la liste est vide")
        else:
            print(sup_someone(D,input("saisir le nom du vendeur : ")))        
    elif choix==7:
        if D=={}:
            print("la liste est vide")
        else:
            print(somme(D))         
    elif choix==8:
        if D=={}:
            print("la liste est vide")
        else:
            print(max_vent(D))         
    elif choix==9:
        if D=={}:
            print("la liste est vide")
        else:
            if D=={}:
                print("la liste est vide")
            else:
                enregistre_ventre(D)
    elif choix==10:
        break
    else:
        print("choix invalide")