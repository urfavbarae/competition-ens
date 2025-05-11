#!02.12.2023
c="hello world"
print(c.capitalize) #!cette methode sert a rendre la premiere lettre du titre en majescule

c="hello world"
print(c.title()) #!cette methode sert a rendre les premiers lettre du titre en majescule

#tranchange (slicing): chaine[posdebut:posfin:step] => extrait une partie  une tranche de la chaine
print(c[:])
#!exemple
c="hello world "
print(c[2:9])
c="hello world "
print(c[1:5:2])
c="hello world "
print(c[1:5:-2])
c="hello world "
print(c[-1:5:-1])
c="hello world "
print(c[2:-1:-3])
c=" hello world "
print(c[-4:-4])
c="hello world "
print(c[-4:0:-1])

#chaine.find(souschaine,position=0):entier => recherche (de la gauche a droite) la souschaine passee en parametre et retourne la position de sa premiere occurence si elle existe sinon elle retourne -1
c="hello world "
print(c.find("wo",4))

#chaine r.find(souschaine,position=-1):entier => recherche(de la droite a gauche) et retourne la position de sa premiere occurence
#!exemple:
c="hello world "
print(c.rfind("ow",-3))
c="hello world "
print(c.rfind("d",-3))

#chaine.index(souschaine,position=0):entier => recherche (de la gauche a droite) la souschaine passee en parametre et retourne la position de sa premiere occurence si elle existe sinon elle declanche exception ValueError
c="hegillgio worgildeg "
print(c.index("gix",3))

#chaine.count(souschaine): entier => retourne le nombre d`occurence de l asouschaine passee en 
print(c.count("gi"))

C="wefert vrwed kw12 ruo    wihwr"

#chaine.replace(anciennenouvelle):chaine=> remplace l`ancienne souschaine par la nouvelle souschaine passe en parametre et retourne une nouvelle chaine 
print(C.replace("gi","XX"))

#chaine.startwith(souschaine)/ chaine.endswith(souschaine):booleen
print(C.startswith("gi"))

#chaine.split(separateur=" ",maxsplit=None) : liste
C="wefert vrwed kw12 ruo    wihwr"
print(C.split())

#glue.join(listedeschaine): chaine
print(".join"(["ahmadi","jelali","yaakoubi"]))

#!to search
#chaine.isdigit
#chaine.isalpha