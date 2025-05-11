j=int(input("saisir le jour : "))
m=int(input("saisir le mois : "))
y=int(input("saisir l'anne : "))

if j>31 or j<1 or m>12 or m<1 or y<0:
    print("un des valeur est incorect")
elif m==2:
    if y%4==0 and not y%100==0 or y%400==0 :
        if j==29:
            print(f"le lendemain est 1/3/{y}")
        elif j<29:
            print(f"le lendemain est {j+1}/2/{y}")
        else:
            print("le mois fevrier a 29 jour")
    else:        
        if j==28:
            print(f"le lendemain est 1/3/{y}")
        elif j<28:
            print(f"le lendemain est {j+1}/2/{y}")
        else:
            print("cette annee le mois fevrier a 28 jour")    
elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    if j==31 and m==12:
        print(f"le lendemain est 1/1/{y+1}")
    elif j==31:
        print(f"le lendemain est 1/{m+1}/{y}")
    else:
        print(f"le lendemain est {j+1}/{m}/{y}")
else:
    if j==30:
        print(f"le lendemain est 1/{m+1}/{y}")
    elif j<30:
        print(f"le lendemain est {j+1}/{m}/{y}")
    else:
        print("un des valeur est incorect")
