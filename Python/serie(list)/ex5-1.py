def hamming(m1,m2):
    if len(m1) != len(m2):
        return -1
    c=0
    for i in range(len(m1)):
        if m1[i]!=m2[i]:
            c+=1
    return c
print(hamming(input("saisir la premiere chaine : "),input("saisir la deuxieme chaine : "))) 