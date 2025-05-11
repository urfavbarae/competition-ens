print("you take all the responsibility if you entred a wrong value")
d1=int(input('entre the first day : '))
m1=int(input('entre the first month : '))
y1=int(input('entre the first year : '))
d2=int(input('entre the second day : '))
m2=int(input('entre the second month : '))
y2=int(input('entre the second year : '))
if y1>y2:
    print(f'{d2}/{m2}/{y2} is older than {d1}/{m1}/{y1}')
elif y2>y1:
    print(f'{d1}/{m1}/{y1} is older than {d2}/{m2}/{y2}')
else:
    if m1>m2:
        print(f'{d2}/{m2}/{y2} is older than {d1}/{m1}/{y1}')
    elif m2>m1:
        print(f'{d1}/{m1}/{y1} is older than {d2}/{m2}/{y2}')
    else:
        if d1>d2:
            print(f'{d2}/{m2}/{y2} is older than {d1}/{m1}/{y1}')
        elif d2>d1:
            print(f'{d1}/{m1}/{y1} is older than {d2}/{m2}/{y2}')
        else:
            print(f'{d1}/{m1}/{y1} is the same as {d2}/{m2}/{y2}')
'''
algorithme
variable 
    d1, m1, y1, d2, m2, y2 : reel
debut
    ecrire("you take all the responsibility if you entred a wrong value")
    ecrire("entre the first date")
    lire(d1,m1,y1)
    ecrire("entre the second date")
    lire(d2,m2,y2)
    si y1>y2 alors
        ecrire("the second date older than the first one")
    sinon
        si y2>y1 alors
            ecrire("the first date older than the second one")
        sinon 
            si y1=y2 alors
                si m1>m2 alors
                    ecrire("the second date older than the first one")
                sinon 
                    si m2>m1 alors
                        ecrire("the first date older than the second one")
                    sinon
                        si d1>d2 alors
                            ecrire("the second date older than the first one")
                        sinon 
                            si d2>d1 alors
                                ecrire("the first date older than the second one")
                            sinon
                                ecrire("the dates are the same")
                            finsi
                        finsi
                    finsi
                finsi
            finsi
        finsi
    finsi
finsi
fin                             
''' 