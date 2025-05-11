sb=float(input("saisir ton salaire de base : "))
if sb>=12000 or sb<=0:
    print("tu n'a aucun prime")
else:
    sf=input("quelle ton sutuation familiale M(mariee), C(celibataire), D(divorce), V(veuf) : ")
    if sf=="m" or sf=="M":
        print(f"ton salaire total est : {sb + 0.20*sb}")
    elif sf=="c" or sf=="C":
        print(f"ton salaire total est : {sb + 0.10*sb}")
    elif sf=="d" or sf=="D" or sf=="V" or sf=="v":
        sfe=input("est ce que tu as des enfant yes or no : ")
        if sfe=="yes":
            print(f"ton salaire total est : {sb + 0.30*sb}")
        elif sfe=="no":
            print(f"ton salaire total est : {sb + 0.10*sb}")
        else:
            print("tu n'a pas entrer un valeur valide")
    else :
        print("un valeur est un valid try later")
'''
algorithme 
variable 
    sb:reel
    sf, sfe: chaine
debut
ecrire("saisir ton salaire de base")
lire (sb)
si sb>12000 alors
    ecrire("tu prend 12000 et tu veut un prime tu es malad au quoi ??!")
sinon
    ecrire("quelle ton sutuation familiale M(mariee), C(celibataire), D(divorce) or V(veuf) : ")
    lire (sf)
    si sf="M" ou sf="m" alors
        ecrire("ton salaire total est : ", sb + 0.20*sb)
    sinon 
        si sf="C" ou sf="c" alors
            ecrire("ton salaire total est :", sb + 0.10*sb)
        sinon
            si sf="D" ou sf="d" ou sf="V" ou sf="v" alors
                ecrire("tu es d'enfant yes or no")
                si sfe="yes" alors
                    ecrire("ton salaire total est :", sb + 0.30*sb)
                sinon
                    si sfe="no" alors
                        ecrire("ton salaire total est :", sb + 0.30*sb)
                    sinon 
                        ecrire("tu as entrer un valeur fausse )
                    fin si
                fin si
            sinon
                ecrire("tu as entrer un valeur invalide")
            fin si
        fin si
    fin si
fin si
fin
'''