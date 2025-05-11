age=int(input("saisir ton age : "))
sex=input("siasir f pour les femme et h pour les homme: ")
if sex!="f" and sex!="F" and sex!="h" and sex!="H":
    print("sex invalid")
elif ( age<18 and sex=="f"or sex=="F" ) or ( age>35 and sex=="f"or sex=="F" ) or (age<20 and sex=="h"or sex=="H" ) :
    print("you don't pay taxes")
else:
    sal=int(input("entre ton salaire : "))
    if (sex=="f" or sex=="F") and sal>0:
        print(f"you need to pay {sal*0.07}")
    elif (sex=="h" or sex=="H") and sal>0:
        print(f"you need to pay {sal*0.1}")
    else:
        print("salaire est negative")