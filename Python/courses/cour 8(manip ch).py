nb=input("saisir le nbr: ")
for i in range(len(nb)):
    print(nb[i],end="|")
    print(i)

"""
algorithme
variable
debut
pour i allant de 0 a longueur(ch)-1
fin 
"""
#regle 1:
""" 
"ahmed"=>["A"|"H"|"M"|"A"|"D"]
"""
#regle 2:
#pour acceder a un caractere : chaine[indice]
#les indices positifs : de 0 a longueur(chaine)-1(de gauche a droit)
#les indice negativfs : de -1 a -longueur(chaine) (de droit a gauche)
#chaque caractere a deux indice un positif et l autre negative
#les fct de manipulation de chaine de caractere
"""
- Longueur(chaine):entier | python len()  
- miniscule(chaine)/majuscu le(chaine)
- code(caractere):entier retourn le code ascii de caract | python ord()
- car(codeascii):caractere retourn le caractere de code ascii | python chr()
- sschaine(chaine,position,nbrcarac{tol daila}):chaine retourn a piece of a chaine ;
- rang(chaine,souschaine,position=0)=> recherche la sous chaine dans la chaine passe en parametre si elle existe la fonction retourne 
l'indice de sa premiere occurence sinon elle retourne -1
"""
#les methode de chaine en python
#la methode est toujours appeler par object: object.methode(parametre)
#toute les methode des chaine retourne des redultat
#chaine.upper()|chaine.lower()
#chaine.isupper()|chaine.islower()=>retourn true or false
#chaine.capitalize(): retourne une nouvelle chaine le premier caracter Maj et le reste miniscul

