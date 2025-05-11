def et_info(ch):
    l=ch.split()

    d={}
    for i in l:
        l1=i.split(";")
        d[l1[0]]=l1[1]+" "+l1[2]
    return d
print(et_info(input("saisir le chaine sous cette forme cef;nom;prenom : ")))