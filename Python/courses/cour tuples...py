#les tuples
#les tuples : liste immutables qui contient des valeurs immutables d'une meme nature
print(dir(tuple))
#declaration d'un tuple:
t=() #tuple vide
t=tuple() #tuple vide
t=(1,5,6,7,8,9,10)
t1=(1,"s",True,[2,3,4],(5,6,7))
t2=5,5.6,59,"hello" #parentheses not needed
#declarer un seul element dans un tuple:
t3=(1,)
print(type(t3))
#affichage d'un seul element dans un tuple:
print(t[3])
#parcourir un tuple:
for i in t:
    print(i) #i prend la valeur de chaque element
#parcourir un tuple par indice:
for i in range(len(t)):
    print(t[i])
#concatenation de tuples:
t4=t+t1
print(t4)
#remplisage d'un tuple:
t5=()
nb=int(input("saisir un nb: "))
#for i in range(nb):
   # t5+=(int(input("saisir un nb: ")),)
print(t5)
#convertir un tuple en liste:
l=list(t)
print(l)
#convertir une liste en tuple:
t6=tuple(l)
#la methode tuple.index(value) => retourne l indice de la valeur passe en parametre de la premiere occurence