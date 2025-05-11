tn=float(input("saisir le tarif normal d'abonement : "))
q=input("""saisir la qualiter de ton abbonnement
        A pour Ancient abonement
        E pour etudiant
        N pour nouveau abonnement
        ET pour etranger : """)
if tn<=0:
    print("tarif unnvalid")   
else:     
    if q=='A' or q=='a':
        print(f'le prix apres remise est {tn-0.15*tn}')
    elif q=='e' or q=='E':
        print(f'le prix apres remise est {tn-0.2*tn}')
    elif q=='n' or q=='N':
        print(f'le prix est le meme tu na acun reuction, leprix est : {tn}')
    elif q=='ET' or q=='et' or q=='Et' or q=='eT':
        print(f'tu est un etranger alors le prix est: {tn+0.2*tn}')
    else:
        print('abonnement anavailable')

"""
algorithme 
Variable
    tn <- reel
    q <- chaine 
debut
ecrire("saisir le tarif normal")
lire(tn)
ecrire("saisir le saisir la qualiter de ton abbonnement
        A pour Ancient abonement
        E pour etudiant
        N pour nouveau abonnement
        ET pour etranger : ")
lire(q)
si q='A' ou q='a' alors
    ecrire('le prix apres remise est :',tn-0.15*tn)
sinon
    si q='e' ou q='E' alors
        ecrire('le prix apres remise est : ',tn-0.2*tn)
    sinon 
        si q='n' ou q='N'alors
            ecrire ('le prix est le meme tu na acun reuction, leprix est :', tn)
        sinon
            si q='ET' ou q='et' ou q='Et' ou q='eT' alors
                ecrire('tu est un etranger alors le prix est: ',tn+0.2*tn)
            sinon
                ecrire('abonnement anavailable')
            finsi
        finsi
    finsi
finsi
fin
"""