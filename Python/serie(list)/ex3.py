l=[]
nb=int(input("saisir le nombre des element que tu va entrer : "))
for i in range(1,nb+1):
    e=int(input("saisir l'element : "))
    l.append(e)
mess="les valeur qui se repete plus de deux fois sont : "
l2=l.copy()
for i in l2:
    if l2.count(i)>=2:
        mess+=str(i)+" "
        for j in range(l.count(i)):
            l2.remove(l2[i])        
print(l)
print(mess)
mess2="les valeur qui ne repete pas sont : "
for i in l2:
    mess2+=str(i)+" "
print(mess2)