#exercice2:
""" def fact(k):
    if k==0:
        return 1
    else:
        return fact(k-1)*k

def produit(n,p):
    if n<p:
        return False
    else:
        facdefac=1
        for i in range(p):
            facdefac*=fact(n-i)
        return facdefac
    
def binomial(n,p):
    return produit(n,p)/p

def tuple_binomi(n):
    t=()
    for i in range(n+1):
        t+=(binomial(n,i),)
    return t
 """
#exercice3:
def replirrend(d):
    nb=int(input("entrer le nombre de elements : "))
    for i in range(nb):
        num=int(input("saisir le nombre rdz : "))
        d[num]={"nom_patient":input("saisir le nom du patient : "),"date":input("saisir la date : "),"type":input("saisir le type : "),"prix":input("saisir le prix")}

def afficher(d):
    for i,j in d.items():
        print(f""" num: {i} - nom_patient: {j["nom_patient"]} - date: {j["date"]} - type: {j["type"]} - prix: {j["prix"]}""")

def modifier(d,num):
    if num in d:
        for i in d[num]:
            if i=="prix":
                d[num][i]=int(input("saisir le nouveau prix : "))
            else:
                d[num][i]=input(f"saisir la nouvelle {i} : ")
    else:
        print("num n'existe pas")
def suprim(d,num):
    if num in d:
        d.pop(num)
    else:
        print("num n'existe pas")

def statist(d):
    dtest={}
    for i in d.values():
        if i["type"] in dtest:
            dtest[i["type"]]+=1
        else:
            dtest[i["type"]]=1
    for j in dtest:
        f=open(".\\old ccs\\stat.txt","a")
        f.write(f"{j} => {dtest[j]} fois \n")
        f.close()
        """ with open(".\\old ccs\\stat.txt","w") as f:
            f.write(f"{j} => {dtest[j]} fois \n")"""
        

while True:
    d={}
    choix=int(input("""
1 - Afficher Locations 
2 - Modifier Location 
3 - Supprimer Location
4 - Afficher la voiture la plus louée
5 - Quitter

Entrez votre choix :
"""))
    if choix==1:
        afficher(d)
    elif choix==2:
        num=int(input("saisir le num : "))
        modifier(d,num)
    elif choix==3:
        num=int(input("saisir le num : "))
        suprim(d,num)
    elif choix==4:
        pass
    elif choix==5:
        break