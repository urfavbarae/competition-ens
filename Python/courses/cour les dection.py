# dictionnaire : sont des entites de type colleection qui organisent les element sous form des pairs <key:value> 
#the key must be unique
#the key can be any type exept the list or dictionary because they are not hashable 
#les dictionnaires sont unisens cle=>valeur et pas valeur=>cle
#la declaration d'un dictionnaire: "{key1:value1,key2:value2}"
d={} #dictionnaire vide
d=dict() #dictionnaire vide
d1={"nom":"ali","age":21,"ville":"tanger"} #dictionnaire non vide
print(d1)
d2={45:"sd",True:"sda","dsa":94} #dic mkharba9a
#dic niveau 1: <scalaire:scalaire>
d3={45:456,32:54,1:32,4:5}
#dic niveau 2: <scalaire:liste/tuple>
d4={"ali":[12,4,12],"ahmed":[12,4,2,],"salma":[4,7,8]}
#dic niveau 3: <scalaire:dictionnaire>
d5={1:{"nom":"ali","age":21,"ville":"tanger"},2:{"nom":"ahmed","age":21,"ville":"tanger"},3:{"nom":"salma","age":21,"ville":"tanger"}}
#affichage d'un element d'un dictionnaire
print(d1["ville"])
#parcourir un dectionnaire:
#1 par cle:
for i in d5: #i prend la cle du dictionnaire
    print(i) #afficher la cle
    print(d5[i]) #afficher la valeur
#la methode dict.keys():retourne liste des cle
print(d5.keys())
#la methode dict.values():retourne liste des valeurs
print(d5.values())
for i in d5.values():
    print(i) #affich chaque valeur
#la methode dict.items():retourne liste des tuples chaque tuple contient le paire <cle:valeur> 
print(d5.items())
for i in d5.items(): #i prend chaque tuple
    print(i) #affich chaque tuple
    print(i[0]) #affich la cle
    print(i[1]) #affich la valeur
for i,j in d5.items(): #i prend la cle et j prend la valeur
    print(i,j)
#modification d'un element:
d5[1]={"nom":"fatma","age":31,"ville":"taroudant"}
print(d5)
#ajout d'un element:
d5[4] = {"nom": "Karim", "age": 25, "ville": "Casablanca"} #car la cle 4 n'existe pas on ajout la cle 4 et sa valeur
print(d5)
#methode update(): permet d'ajouter un element ou plusieurs elements au dictionnaire //prend un dictionnaire en parametre dict.update(d)
d5.update({"sara":{"nom":"sara","age":21,"ville":"tanger"}})
d4.update(d1)
print(d4)
print(d5)
#remplissage d'un dictionnaire:
#the easiest way:
"""#niveau 1: <scalaire:scalaire>
prd={}
np=int(input("saisir le nombre de produit: "))
for i in range(1,np+1):
    prd[input("saisir le ref du produit: ")] = int(input("saisir le prix du produit: "))
print(prd)
#niveau 2: <scalaire:liste/tuple>
prd2={}
np2=int(input("saisir le nombre de produit: "))
for i in range(1,np2+1):
    prd2[input("saisir le ref du produit: ")] = [input("saisir le nom du produit: "),int(input("saisir le prix du produit: ")),int(input("saisir le quantite du produit: "))]
print(prd2)
#niveau 3: <scalaire:dictionnaire>
prd3={}
np3=int(input("saisir le nombre de produit: "))
for i in range(1,np3+1):
    prd3[input("saisir le ref du produit: ")] = {"nom":input("saisir le nom du produit: "),"prix":int(input("saisir le prix du produit: ")),"qte":int(input("saisir le quantite du produit: "))}
print(prd3)"""
#the way best:
#niveau 1: <scalaire:scalaire>
""" prd={}
np=int(input("saisir le nombre de produit: "))
for i in range(1,np+1):
    ref=input("saisir le ref du produit: ")
    prd[ref] = int(input("saisir le prix du produit: "))
print(prd) """
#niveau 2: <scalaire:liste/tuple>
""" prd2={}
np2=int(input("saisir le nombre de produit: "))
for i in range(1,np2+1):
    ref=input("saisir le ref du produit: ")
    prd2[ref] = [input("saisir le nom du produit: "),int(input("saisir le prix du produit: ")),int(input("saisir le quantite du produit: "))]
print(prd2) """
#niveau 3: <scalaire:dictionnaire>
""" prd3={}
np3=int(input("saisir le nombre de produit: "))
for i in range(1,np3+1):
    ref=input("saisir le ref du produit: ")
    prd3[ref] = {"nom":input("saisir le nom du produit: "),"prix":int(input("saisir le prix du produit: ")),"qte":int(input("saisir le quantite du produit: "))}
print(prd3) """

#la methode dict.pop(cle) : supprime l element dont lacle passe en parametre 
#methode dict.popitem() : supprime le dernier element du dictionnaire
#methode dict.clear() : vide le dictionnaire
""" d1={"AHMADI": 12 ,"ABDELLAH": 13 ,"HASSAN": 14,"MOHAMED": 15,"KHALED": 16}
print("avant" ,d1)
d1.popitem()
print("apres" ,d1) 
for i in d1 :
    if d1 [i]<10:
        d1.pop(i)
print(d1)
 """
#methode de supretion de plusieur elements:
#exemple 1: supresion de tous les elements dont la valeur est inferieure a 10
""" dc=d1.copy()
for i in dc:
    if dc[i]<10:
        d1.pop(i)
#methode 2:
l=[]
for i in d:
    if d[i]<10:
        l.append(i)
for i in l:
    d1.pop(i) """

#methode dict.get(cle,value) / dict.setdefault(cle,value) :
#value: valeur par defaut si la cle n'existe pas
d10={"AHMADI": 12 ,"ABDELLAH": 13 ,"HASSAN": 14,"MOHAMED": 15,"KHALED": 16} 
print(d10.get("MOHAMD","non existe"))

#metode dict.fromkeys(listecle,value=None) : retourn un dictionnaire avec les cle de la liste et la valeur par defaut (les valeur son unifiere)
print(dict.fromkeys([1,2,3,4,5],"salamo alaykom"))
