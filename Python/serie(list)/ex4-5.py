def ordre(ch):
    ch1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ch2="abcdefghijklmnopqrstuvwxyz"
    ch3="0123456789"
    l=list(ch)
    l1,l2,l3,l4=[],[],[],[]
    for i in l:
        if i in ch1:
            l1.append(i)
        elif i in ch2:
            l2.append(i)
        elif i in ch3:
            l3.append(i)
        else:
            l4.append(i)
    l1=sorted(l1)
    l2=sorted(l2)
    l3=sorted(l3)
    l4=sorted(l4)

    l=l2+l1+l3+l4
    ch="".join(l)
    return ch
print(ordre("akdjf,.mfsdj,safsdfGVBSdd11353"))