pht=float(input("saisir le prix hors taxes : "))
nba=int(input("saisir le nombre d'articles acheter : "))
ttva=float(input("saisire le taux de tva : "))
print(f'le prix TTC : {pht*nba*(1+ttva)}')