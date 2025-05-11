email=input("saisir ton e-mail : ")
for i in email:
    if i=="@":
        break
    print(i,end="")

