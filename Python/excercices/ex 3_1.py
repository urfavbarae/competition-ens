import math
a=float(input("saisir la valeur de a : "))
b=float(input("saisir la valeur de b : "))
c=float(input("saisir la valeur de c : "))
if a==0:
    if b==0:
        print("l'equation n'a pas de solution")
    else:
        print(f'la solution est {-c/b}')
else:
    de= pow(b,2)-4*a*c
    if de<0:
        print("l'equation n'a pas de solution en R")
    elif de==0:
        print(f"l'equation a une seul solution qui est : {-b/(2*a)}")
    else:
        print(f"l'equaion a deux solution X1={-b-math.sqrt(de)/(2*a)} X2={-b+math.sqrt(de)/(2*a)}")    


