import os
f=open("carsrent.txt","r")
d={}
size=os.path.getsize("carsrent.txt")
while f.tell()!=size:
    l=f.readline().split(";")
    d[l[0]]={"nom_client":l[1],"datelocation":l[2],"immatruculation":l[3],"marque":l[4].rstrip()}
for i in d:
    print(d[i])
