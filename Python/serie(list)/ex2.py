
l=[]
nb=int(input("saisir le nombre des element que tu va entrer : "))
for i in range(1,nb+1):
    e=input("saisir l'element : ")
    l.append(e)
stock=""
for i in l:
    for j in i:
        stock+=str(ord(j))
print(stock)