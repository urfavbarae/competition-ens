def remp_tuple(l,c):
    if c<=0 or c!=l:
        return False
    else:
        lr=[]
        for i in range(1,l+1):
            l1=[]
            for j in range(1,c+1):
                l1.append(int(input(f"saisir la valeur de col {j} de la ligne {i} : ")))
            lr.append(l1)
        c=0
        for i in lr:
            lr[c]=tuple(i)
            c+=1
        lr=tuple(lr)
        return lr
def display(t):
    for i in t:
        for j in i:
            print(j,end="\t")
        print("\n")

def sum_diagonal(t):
    s=0
    for i in range(len(t)):
        s+=t[i][i]
    return s

def trian_sup(t):
    if t[-1][0]==0 and t[-1][1]==0:
        return True
    else:
        return False

t=remp_tuple(int(input("saisir le nombre de ligne: ")),int(input("saisir le nombre de colum: ")))

display(t)
print(f"la somme de diagonal principale est {sum_diagonal(t)}")
if trian_sup(t):
    print("c'est un trangle superieur")
else:
    print("ce n'est pas un triangle superieur")