#list bidimensionelle
l=[[1,2,3,5],[4,5,6],[7,8,9],["a","b","c"]]
#matrice: est une liste bidimensionelle qui contient des listes qui contiennent des elements d'une meme nature et meme taille
m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#affichage d'un element:
print(m[1][2])
print(l[3][2])
#parcourir une liste bidimensionelle par valeur:
for i in l:
    for j in i:
        print(j)
#parcourir une liste bidimensionelle par indice:
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j])
#remplir une liste bidimensionelle:
l2=[]
n=int(input("saisir la taille de la liste : "))
for i in range(n):
    l2.append([])
    m=int(input("saisir la taille de la liste : "))
    for j in range(m):
        l2[i].append(input("saisir un element : "))
print(l2)