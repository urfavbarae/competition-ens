n=int(input("saisir n : "))
un_2=-1
un_1=1
c=0
for i in range(0,n+1):
    if i==0:
        print("U0=-1")
    elif i==1:
        print("U1=1")
    else:
        un=i*(3*un_1+un_2)
        print(f"u{i}={un}")
        un_2=un_1
        un_1=un
        