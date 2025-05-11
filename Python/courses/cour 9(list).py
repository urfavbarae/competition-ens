
#!15.12.2023
###########################################!           les tableaux            ##########################################################
# les types scalaires des variables : entier / reel / booleen / chaine
# les types collections des variables : ensemble des variables ; chaue sera stockee dans une case => 1- les listes / les tuples / dictionnaires / les datasets / dataframes / pandas / les numpy / hashmaps ...
#...=> les iterables / les enumerables 
# [v1 .....v6] : iteration c est le fait de passer d un element a un autre

# les listes : se sont des entites ui stockent des valeurs ( des  elements) d`une maniere indexes (chauque element a un indice p/n) et qui peuvent 
#1- la declaration d'une liste:
#l=[] -> liste vide 
#l= list() -> liste vide
# la fonction liste (iterable): liste => retourne une liste contenant
#les elements de l'iterable passe en parametre , si on ne precise le parametre
# la fonction list() cree une liste vide => []
l=[3,645,64,54,67,45,12,84,231,987]
l=["654","654","sdad"]
l=[64,"saiohfd",True,[1,1,1,1],{"sd":98}]
# la fonction len(list) : entier => retourne le nombre des elements d'une list 
# affichage d'un seul element : liste[indice]
print(l[2])
#parcourir la list : iteration
for i in l:
    print(i) 
    # parcourir la list (itteration oar indice)
for i in range(len (l)):
    print(i)
#tranchage / slicing:
    print(l[-2:1:-1])
#les listes sont des entites modifiable : on peut un element ou 
#une tranch des elements soit on peut etendre la liste ou la restreindre
#la modification d'un element : list[indice] = nouvelle_valeur
l1=[45,"odkslf",True,65.54,875]
print("avant",l1)
l1[-4]="AAA"
print("apres",l1)
#la modification d'un tranche: list[id:if:s] = nouvelle valeur(iterable)
l1[-2:-6:-1]=[54,45,1,2]
l1[-2:-6:-1]="llkd"
print("apres2",l1)
print(dir(list))
# methode dans les liste ('append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort')
#la methode list.append(valeur) : ajoute a la fin de la liste qui appelle la valeur passe au parametre
print("avant",l1)
l1.append("XXX") # only accept one parametre
print("apres3",l1)
#l methode list.insert(position,valeur) : ajoute a la position passe en parametre
print("avant",l1)
l1.insert(2,"insert")
print("apres3",l1)
#la methode list.extend(iterable) => ajoute a la fin (concatene l'iterable passe en parametre a la liste qui appelle)
print("avant",l1)
l1.extend((3,6))

#la concatenation l3=l1+12
l2=[21,32,5,51,511,22]
l3=l1+l2
print("l3",l3)
#suppresion : par indice :
#mot cle del liste[indice]
l2=[21,32,5,51,511,22]
del l2[5]
print("l2 apres",l2)
del l2[1:3:1]
print("l2 apres2",l2)
#methode list.pop(indice)
l2.pop(2)
print(l2)
#la methode list.remove(valeur) => supresion oar valeur
l2.remove(51)
print(l2)
#la methode list.clear() => vider la list
l2.clear()
print(l2)
#1- la suppression de toutes les occurences d'une valeur x
l5=[5,6,9,6,5,47,4,7,8,5,2,3,2,3,2,3,1,4,1,2]
for i in range(l5.count(5)):
    l5.remove(5)
print(l5)
#2- la suppression de tout elements qui repsente a une condition
l5=[5,6,9,6,5,47,4,7,8,5,2,3,2,3,2,3,1,4,1,2]
#using while (recomended)
i=0 
while i<len(l5):
    if l5[i]<5:
        l5.remove(l5[i])
    else:
        i+=1
print(l5)
#using for
cp=0
for i in l5:
    if i<5:
        cp+=1
for i in range(cp):
    for i in l5:
        if i<5:
            l5.remove(i)
        continue
print(l5)
# la methode index(valeur) => retourne l indice de la valeur passe en parametre de la premiere occurence de 
#la valeur passe en parametre s'il existe sinon retourne valueerror
print(l5.index(8))
#la methode list.reverse() => inverse la liste
print("avant",l5)
l5.reverse()
print("apres",l5)
#la methode list.sort(key=None, reverse=False) => trie la liste selon le criter passe en parametre et selon le sens de tri
print("avant",l5)
l5.sort()
print("apres",l5)
l5.sort(reverse=True)
print("apres2",l5)  
#la fonction sorted(iterable, key=None, reverse=False) => trie la liste selon le criter passe en parametre et selon le sens de tri
print(sorted("barae boulaich"))
#copie d'une liste:
#la methode list.copy() => copie la liste
l6=l5.copy() #un copie de valeur
print(l6)
#en utilisant les tranche:
l7=l5[:]    #un copie de valeur
#en utilisant les affectation:
l8=l5 #un copie d'adress / pointeur vers la meme adresse
#la methode list.count(valeur) => retourne le nombre d'occurence de la valeur passe en parametre
l5.count(5)

