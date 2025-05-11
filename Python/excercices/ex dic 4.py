dtest={"stg3":{"M01":12,"M02":11,"M03":13},"stg2":{"M01":9,"M02":12,"M03":11},"stg1":{"M01":18,"M02":12,"M03":12}}

def remp_note(d):  
    n=int(input("saisir le nombre de stagier : "))
    for i in range(1,n+1):
        d[f"stg{i}"]={"M01":int(input(f"saisir la note 1 de stagier {i}: ")),"M02":int(input(f"saisir la note 2 de stagier {i}: ")),"M03":int(input(f"saisir la note 3 de stagier {i}: ")),}
    return d

def moy(d):
    d2={}
    for i in d:
        d2[i]=sum(d[i].values())/len(d[i])
    return d2

def remove(d,st):
    if st in d:
        d.pop(st)
    else:
        print("ce stagiaire n'existe pas")
    

def moyc(d):
    d2=moy(d)
    m=0
    for i in d2.values():
        m+=i
    m=m/len(d2)
    return m

def tri_st(d):
    l=sorted(d.keys())
    d1={}
    for i in range(len(l)):
        d1[l[i]]=d[l[i]]
    return d1

def mod_note(d,st):
    d[st]["M01"]=int(input("saisir la nouvelle note 1 : "))
    d[st]["M02"]=int(input("saisir la nouvelle note 2 : "))
    d[st]["M03"]=int(input("saisir la nouvelle note 3 : "))
    return d

def premi(d):
    return max(moy(d),key=moy(d).get)

    
def notemax(d):
    for i in d:
        d[i]=max(d[i].values())
        for j in d[i]:
            if d[i][j]==max(d[i].values()):
                print(f"le stagiaire {i} a eu la note maximale {max(d[i].values())} dans le module : {j}")
    return d

def moy_clas_m(d,m):
    l=[]
    for i in d:
        l.append(d[i][m])
    m=sum(l)/len(l)
    return m

choix=0
d={}
while choix!=8:
    choix=int(input("""
-------------Menu------------- 
1 : Remplir les notes
2 : Afficher la moyenne de chaque stagiaire .
3 : Trier le dictionnaire des notes .
4 : Modifier les notes d'un stagiaire .
5 : Afficher le premier de la classe .
6 : Supprimer un stagiaire .
7 :Afficher la moyenne de la classe pour une module
8: Quittez le programme
Tapez votre choix : """))
    if choix==1:
        d=remp_note(d)
    elif choix==2:
        if d=={}:
            print("la liste est vide")
        else:
            print(moy(d))
    elif choix==3:
        if d=={}:
            print("la liste est vide")
        else:
            print(tri_st(d))
    elif choix==4:
        if d=={}:
            print("la liste est vide")
        else:
            print(mod_note(d,input("saisir le nom du stagiaire : ")))
    elif choix==5:
        if d=={}:
            print("la liste est vide")
        else:
            print(premi(d))
    elif choix==6:
        if d=={}:
            print("la liste est vide")
        else:
            print(remove(d,input("saisir le nom du stagiaire : ")))
    elif choix==7:
        if d=={}:
            print("la liste est vide")
        else:
            print(moy_clas_m(d,input("saisir le nom du module : "))) 
    elif choix==8:
        print("au revoir")
    else:
        print("choix invalide")