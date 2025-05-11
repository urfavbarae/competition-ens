mp=float(input("saisir le mantant acheter : "))
if mp<0:
    print('montant invalide')
elif mp>5000:
    print(f"le prix apres reduction {mp-0.2*mp}")
elif mp>3000:
    print(f"le prix apres reduction {mp-0.15*mp}")
elif mp>1000:
    print(f"le prix apres reduction {mp-0.1*mp}")
else:
    print("cette montant n'a aucun reduction")