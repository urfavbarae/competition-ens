def maxi(a,b):
    if a>b:
        print(f"{a} est plus grand de {b}")
    elif a<b:
        print(f"{b} est plus grand de {a}")
    else:
        print(f"{a} est {b} sans egaux")
maxi(int(input("saisir les deux nombre : ")),int(input()))