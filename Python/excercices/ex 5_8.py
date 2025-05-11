def calc(a,b,op):
    if op=="+":
        return a+b 
    elif op=="-":
        return a-b
    elif op=="x":
        return a*b
    elif op=="/":
        if b==0:
            return "b est null"
        else:
            return a/b
    else:
        return "op invalide"
print(calc(int(input("saisir deux nombre: ")),int(input()),input("entrez l'operation que tu veux")))
