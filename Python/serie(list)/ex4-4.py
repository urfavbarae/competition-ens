def prefixadn(mots):
    ch="ACGT"
    l=list(mots)
    l1=l[0:4]
    l1=sorted(l1)
    ch2="".join(l1)
    if ch2==ch:
        return True
    else:
        return False
print(prefixadn(input("entrer la chaine : ")))

