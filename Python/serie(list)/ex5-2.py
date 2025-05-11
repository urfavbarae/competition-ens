def rempl(n):
    l = []
    for i in range(n):
        l.append([])
        m = int(input("saisir la taille de la liste : "))
        for j in range(m):
            l[i].append(input("saisir un element : "))
    return l
l1=rempl(int(input("saisir la taille de la liste global: ")))