ppa=5
ppb=2.5
ppc=3
ppd=10
ppe=7 
nba=int(input("saisir le nombre d'article acheter por le produit A:"))
nbb=int(input("saisir le nombre d'article acheter por le produit B:"))
nbc=int(input("saisir le nombre d'article acheter por le produit C:"))
nbd=int(input("saisir le nombre d'article acheter por le produit D:"))
nbe=int(input("saisir le nombre d'article acheter por le produit E:"))
pht= ppa*nba + ppb*nbb + ppc*nbc + ppd*nbd+ ppe*nbe
pttc= pht*(1 + 0.2)
ttva= pttc-pht
print(f"le prix hors taxe est: {pht}")
print(f"les taxes ajouter sont: {ttva}")
print(f"le prix ttc est: {pttc}")