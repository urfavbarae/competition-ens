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
    
l=remp_list(int(input("saisir le nombre de ligne: ")),int(input("saisir le nombre de colum: ")))
print("Les points cols du tableau sont : ",end=" ")
ind=0
for i in l:
    a=min(i)
    index=i.index(a)
    c=0
    for j in l:
        if j[index]>a:
            c+=1
    if c==0:
        print(f"l[{ind}][{index}]={a}")
    ind+=1