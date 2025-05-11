def remp_list(l,c):
    if c<=0 or c!=l:
        return False
    else:
        lr=[]
        for i in range(1,l+1):
            l1=[]
            for j in range(1,c+1):
                l1.append(int(input(f"saisir la valeur de col {j} de la ligne {i} : ")))
            lr.append(l1)
        return lr

li=remp_list(int(input("saisir le nombre de ligne : ")),int(input("saisir le nombre de colonne : ")))
lt=[]
for i in li:
    s=0
    for j in i:
        s+=j
    lt.append(s)
c=0
for i in range(len(li)):
    s=0
    for j in range(len(li)):
        s+=li[j][c]
    lt.append(s)
    c+=1
d=0
for i in range(len(li)):
    d+=li[i][i]
lt.append(d)
d=0
for i in range(len(li)):
    d+=li[i][-i+1]
lt.append(d)
def test(l):
    t=l[0]
    for i in l:
        if i!=t:
            return False
    return "la liste est une matrice magique"

print(test(lt))