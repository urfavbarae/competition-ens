def sommecon(ch):
    l=[]
    l=ch
    i1=""
    #verifier la chaine si elle contient seulement des "+" et des numeros
    c="123456789+0"
    for i in ch:
        if i not in c:
            return -1
    for i in l:
        if i=="+" and i1=="+":
            return -1
        i1=i
    if l[0]=="+" or l[-1]=="+":
        return -1
    else:
        somme=0 #65+54+1+874+54
        l1=ch.split("+")
        for i in l1:
            somme+=int(i)
        return somme
print(sommecon(input("saisir la chaine : ")))