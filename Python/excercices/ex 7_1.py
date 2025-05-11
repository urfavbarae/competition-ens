l=[]
n=int(input("saisir le nombre des element que tu va entrer"))
for i in range(1,n+1):
    a=float(input("etntrez la valeur"))
    l.append(a)
print(l)
nb0=l.count(0)
for i in (1,nb0):
    l.remove(0)
print(l)
i=1
while i<len(l):
    if l[i]<10:
        l.remove

