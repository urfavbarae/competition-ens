def date(d,m,y):
    if (d<31 and (m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12)) or (d<30 and (m==4 or m==6 or m==9 or m==11)) or (m==2 and (y%4==0 and not y%100==0 or y%400==0))  :
        return "date correct"
    else:
        return "date uncorrect"
print(date(int(input("saisir le jour")),int(input("saisir le mois")),int(input("saisir l anne"))))