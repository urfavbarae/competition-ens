t=()
n=int(input("saisir le nombre des element que tu va entrer"))
for i in range(1,n+1):
    t+=(int(input("etntrez la valeur: ")),)
print(t)
l=list(t)
l.reverse()
vmin=min(l)
l[l.index(vmin)]=l[-1]
l[-1]=vmin
l.reverse()
t=tuple(l)
print(t)
