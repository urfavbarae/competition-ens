notem=float(input("saisir la note de math : "))
notep=float(input("saisir la note de physique : "))
notes=float(input("saisir la note de SVT : "))
notef=float(input("saisir la note de francais : "))
notea=float(input("saisir la note de anglais : "))
moy=(notem+notep+notes+notef+notea)/5
if notem<=20 and notep<=20 and notes<=20 and notef<=20 and notea<=20 and notem>=0 and notep>=0 and notes>=0 and notef>=0 and notea>=0:
    if moy>=16:
        print("votre moyenne est",moy)
        print("votre mension est tres bien")
    elif moy>=14:
        print("votre moyenne est",moy)
        print("votre mension est bien")
    elif moy>=12:
        print("votre moyenne est",moy)
        print("votre mension est assez bien")
    elif moy>=10:
        print("votre moyenne est",moy)
        print("votre mension est passable")   
    elif moy<10 and moy>0:
        print("votre moyenne est",moy)
        print("votre mension est ajournee")
    else :
        print("tu as entrez un valeur negative")
    print("la plus petit moyen est:",min(notem, notea, notef, notes, notep))
    print("la plus grand moyen est:",max(notem, notea, notef, notes, notep))
else:
    print("la note doivent etre entre 0 et 20")
 
