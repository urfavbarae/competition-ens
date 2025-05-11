"""# Saisir la chaine
chaine = input("Entrez une chaine de caractères : ")

# Initialiser le dictionnaire
dico = {}

# Parcourir la chaine
for car in chaine:
  # Si le caractère est déjà dans le dictionnaire, incrémenter sa valeur
  if car in dico:
    dico[car] += 1
  # Sinon, ajouter le caractère au dictionnaire avec la valeur 1
  else:
    dico[car] = 1

# Afficher le dictionnaire
print(dico)
"""
c=input("entrez une chaine")
s=""
for i in c:
    if i not in s:
        print(f"{i} : {c.count(i)} fois")
        s+=i 