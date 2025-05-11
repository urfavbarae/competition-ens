l=[]
nb=int(input("saisir le nombre des element que tu va entrer : "))
for i in range(1,nb+1):
    e=int(input("saisir l'element : "))
    l.append(e)
nbr=int(input("saisir le nombre de remplacement : "))
for i in l:
    if l.count(i)>=3 and l[i]!=nbr:
        for j in range(len(l)):
            if l[j]==i:
                l[j]=nbr
print(l)
#2. min
i=0 
m=min(l)
while i<len(l):
    if l[i]==m:
        l.remove(l[i])
    else:
        i+=1
print("after remove min",l)
#3. remove the first max element in the list
l.reverse()
l.remove(max(l))
l.reverse()
print("after remove last max",l)


        