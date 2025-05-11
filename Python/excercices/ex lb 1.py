def remp_list(l,c):
    if c<=0 or l<=0:
        return False
    else:
        lr=[]
        for i in range(1,l+1):
            l1=[]
            for j in range(1,c+1):
                l1.append(int(input(f"saisir la valeur de col {j} de la ligne {i} : ")))
            lr.append(l1)
        return lr
def aff_li(l):
    for i in l:
        print(i)

def somme_list(l):
    s=0
    for i in l:
            s+=sum(i)
    print(s)

def nb_positive(l):
    n=0
    for i in l:
        for j in i:
            if j>0:
                n+=1
    return n

def som2d(l):
    c=0
    for i in l:
        sp=0
        sn=0
        c+=1
        for j in i:
            if j>0:
                sp+=j
            else:
                sn+=j
        print(f"la somme positive de la ligne {c} est : {sp} et la somme négative est : {sn}")
    
def max_el(l):
    m=0
    for i in l:
        for j in i:
            if j>m:
                m=j
    return m

def inv(l):
    nl=int(input("saisir le nombre de ligne : "))
    for i in range(len(l[nl])):
        l[nl][i]=1/int(l[nl][i])
    return l

li=remp_list(int(input("saisir le nombre de ligne : ")),int(input("saisir le nombre de colonne : ")))
aff_li(li)
somme_list(li)
print(nb_positive(li))
som2d(li)
print(max_el(li))
li2=inv(li)
print(li2)