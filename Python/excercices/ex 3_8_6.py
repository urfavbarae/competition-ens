prix=float(input('saisir le prix unitaire : '))
q=int(input('saisir la quantite acheter : '))
cat=int(input('saisir la categorie du produit : '))
if prix<=0 :
    print('le prix est negative')
elif q<=0 :
    print('quantite est null ou negative')
elif cat<0 :
    print('categorie invalid')
else:
    if cat==0 or cat==1 :
        print(f'le prix total ttc est {(prix*q)*(1+0.06)} , le tax unclue {prix*0.06}')
    elif cat==2 or cat==3 :
        print(f'le prix total ttc est {(prix*q)*(1+0.09)} , le tax unclue {prix*0.09}')
    elif cat>=4 or cat<7 :
        print(f'le prix total ttc est {(prix*q)*(1+0.15)} , le tax unclue {prix*0.15}')
    else:
        print(f'le prix total ttc est {(prix*q)*(1+0.2)} , le tax unclue {prix*0.2}')


    