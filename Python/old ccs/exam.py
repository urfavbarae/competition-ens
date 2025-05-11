dtest={100:["simple","libre",300,{},0],200:["simple","occupee",100,{"nom_occ":"ahmadi"},3],300:["Double","occupee",400,{"nom_occ":"rachidi","comp":"fatimi"},2]}

def remplir_chambre():
    chambres={}
    cle=""
    while cle!="n" or cle!="N":
        occ={}
        nb_nuit=0
        cle=input("saisir le numero de chambre: ")
        typ=input("saisir le type du chambre : ")
        etat=input("saisir l'etat de chambre : ")
        price=int(input("saisir le prix du chambre : "))
        if etat=="occupee":
            nb_person=int(input("saisir le nombre de personne ocuppant"))
            for i in range(nb_person):
                if i==0:
                    occ["nom_occ"]=input("saisir le nom d'occupant : ")
                else:
                    occ[f"compagnon{i}"]=input(f"saisir le nom de compagnon {i} : ")
            nb_nuit=int(input("saisir le nombre de nuit : "))
        chambres[cle]=[typ,etat,price,occ,nb_nuit]
    return chambres        

#exercice 2:
def afficher_chambres(chambres):
    for i in chambres:
        if chambres[i][1]=="occupee":
            print(f"""num du chambre: {i} | type du chambre: {chambres[i][0]} | etat du chambre: {chambres[i][1]} | prix du chambre: {chambres[i][2]}
infos des occupant: {chambres[i][3]} | nombre de nuit occupee: {chambres[i][4]}""")
        else:
            print(f"""num du chambre: {i} | type du chambre: {chambres[i][0]} | etat du chambre: {chambres[i][1]} | prix du chambre: {chambres[i][2]}""")

#exercice 3:
def rechercher_chambres(chambres,num):
    if num in chambres:
        return 1
    else:
        return 0

#exercice 4:
def supprimer_chambres(chambres,num):
    if num in chambres:
        chambres.pop(num)
    else:
        print("ERROR chambre introuvable")

#exercice 5:
def nombres_occupants(chambres):
    nb_occ=0
    for i in chambres:
        if chambres[i][1]=="occupee":
            nb_occ+=len(chambres[i][3])
    return nb_occ

#exercice 6:
def montant_payee(chambres):
    for i in chambres:
        if chambres[i][1]=="occupee":
            print(f'le chambre {i} d\'occupant {chambres[i][3]["nom_occ"]} doivent paye {chambres[i][2]*chambres[i][4]}')

#exercice 7:
def trie(chambres):
    l=[]
    chambres2={}
    for i in chambres:
        l.append(chambres[i][2])
    l.sort()
    for i in l:
        for j in chambres:
            if i==chambres[j][2]:
                chambres2[j]=chambres[j]
    return chambres2
print(trie(dtest))
#exercice 8:
def statistiques(chambres):
    d={}
    for i in chambres:
        if chambres[i][0] in d:
            d[chambres[i][0]]+=1
        else:
            d[chambres[i][0]]=1
    return d

#exercice 9:
def enregistrer_chambres(chambres):
    f=open("chambres.txt","a")
    for i in chambres:
        if chambres[i][1]=="occupee":
            f.write(f'chambre numero: {i} | Type: {chambres[i][0]} | Etat: {chambres[i][1]} | Prix: {chambres[i][2]} DH | Nom Occupant: {chambres[i][3]["nom_occ"]} | nombre nuites: {chambres[i][4]} \n')
        else:
            f.write(f"chambre numero: {i} | Type: {chambres[i][0]} | Etat: {chambres[i][1]} | Prix: {chambres[i][2]} DH | Nom Occupant: no one | nombre nuites: 0 \n")

#exercice 10:
chambres=dtest
choix=0
while choix!=8:
    choix=int(input("""
===========menu============
1- Remplir Chambres
2- Afficher Chambre
3- Supprimer Chambre
4- Nombre total des occupants
5- Afficher montant total a payer
6- Trier les chambres selon le prix
7- Statique des etats
8- Enregistrer chambres
9-Quitter

"""))
    if choix==1:
        chambres=remplir_chambre()
    elif choix==2:
        if chambres=={}:
            print("tu doit remplir les information")
        else:
            afficher_chambres(chambres)
    elif choix==3:
        if chambres=={}:
            print("tu doit remplir les information")
        else:
            supprimer_chambres(chambres,int(input("saisir le numero de chambre que tu doit supprimer")))
    elif choix==4:
        if chambres=={}:
            print("tu doit remplir les information")
        else:
            print(nombres_occupants(chambres))
    elif choix==5:
        if chambres=={}:
            print("tu doit remplir les information")
        else:
            montant_payee(chambres)
    elif choix==6:
        if chambres=={}:
            print("tu doit remplir les information")
        else:
            trie(chambres)
    elif choix==7:
        if chambres=={}:
            print("tu doit remplir les information")
        else:
            statistiques(chambres)
    elif choix==8:
        if chambres=={}:
            print("tu doit remplir les information")
        else:
            enregistrer_chambres(chambres)
    elif choix==9:
        break
    else:
        print("choix invalid")








    








