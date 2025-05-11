def facto(x):
    if x==0:
        return 1
    else:
        p=1 
        for i in range(1,x+1):
            p*=i
        return p
n=int(input("saisir n: "))
u0=1
vn=0
char=""
for i in range(0,n+1):
    if i==0:
        print(f"U0=1",end=" , ")
    elif i==1:
        print("U1=1",end=" , ")
        char="V1=1 , "
    else:
        un=u0*facto(i-1)
        print(f"U{i}={un}",end=" , ")
        vn+=un/2**i
        char+="V"+str(i)+"="+str(vn)+" , "
        u0=un
print()
print(char)