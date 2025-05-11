hd=int(input("saisir l'heure de depart : "))
md=int(input("saisir la minute de depart : "))
ha=int(input("saisir l'heure d'arivee : "))
ma=int(input("saisir la minute d'arivee : "))
if hd>23 or hd<0 or ha>23 or ha<0 or md>60 or md<0 or ma>60 or ma<0 :
    print("heure invalide")
elif hd<ha :
    hdt=hd*60+md
    hat=ha*60+ma
    dtmm=hat-hdt
    dth=dtmm//60
    dtm=dtmm%60
    print(f"la duree du trajet est {dth}h : {dtm}min")
elif hd>ha :
    ht1=(24*60)-(hd*60+md)
    ht2=ha*60+ma
    mtt=ht1+ht2
    dth=mtt//60
    dtm=mtt%60
    print(f"la duree du trajet est {dth}h : {dtm}min")
else:
    if md<ma:
        print(f"la duree de trajet est {ma-md}min")
    elif md>ma:
        ht1=(24*60)-(hd*60+md)
        ht2=ha*60+ma
        mtt=ht1+ht2
        dth=mtt//60
        dtm=mtt%60
        print(f"la duree du trajet est {dth}h : {dtm}min")
    else:
        print("tu as entree la meme date")