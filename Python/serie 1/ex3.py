min=int(input("saisir les minutes : "))
sec=int(input("saisir les second : "))
while min<0:
    min=int(input("saisir les minutes (ne peux pas etre negative):"))
while sec>=60 or sec<0:
    sec=int(input("saisir les second (ne depasse pas 60 et n'est pas negative): "))
if min==0 and sec==0:
    print("conteur est null 00:00")
t=min*60+sec
for i in range(1,t+1):
    if sec>0:
        sec-=1
        print(f"{min}:{sec}")
    else:
        sec=59 
        min-=1
        print(f"{min}:{sec}")
print("stop")

"""
algorithme
variable
    min,sec,t : entier
debut 
ecrire("saisir les minutes puis les second: ")
lire(min,sec)
tantque min<0 alors
    ecrire("saisir les minutes (ne peux pas etre negative)")
    lire(min)
fintantque
tantque sec<0 ou sec>=60 alors
    ecrire("saisir les minutes (ne peux pas etre negative)")
    lire(min)
fintantque
si min=0 et sec=0 alors
    ecrire("conteur est null 00:00")
finsi
t<-min*60+sec
pour i allant de 1 a t
    si sec>0 alors
        sec<-sec-1
        ecrire(min,":",sec)
    sinon
        min<-min-1
        ecrire(min,":",sec)
    finsi
finpour
ecrire("stop")
fin

"""
    