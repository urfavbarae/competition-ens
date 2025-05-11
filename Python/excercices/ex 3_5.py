cat=input("saisir ton categorie A ou B ou C : ")
nb=int(input("combien des livres tu as prendre : "))
if cat!="A" and cat!="B" and cat!="C":
    print("categorie anavailable")
elif cat=="A" and nb<5 :
    print("tu peut avoir le livre pour un duree de 20 jours")
elif cat=="B" and nb<5 :
    print("tu peut avoir le livre pour un duree de 30 jours")
elif cat=="C" and nb<5 :
    print("tu peut avoir le livre pour un duree de 45 jours")
else:
    print("tu as le max de livre possible")
